
from rest_framework import serializers
import carriers.models as models
import users.models as users_models
import users.serializers as users_serializers
from users.utils import Util
from rest_framework.validators import UniqueValidator
# import files.serializers as files_serializers
from users.models import User, Company
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
from django.urls import reverse
import jwt
from django.utils import timezone
from datetime import datetime, timedelta
class CarrierSerializers(serializers.ModelSerializer):
    """Plans by dates

    Args:
        serializers (_type_): _description_
    """
    company = users_serializers.CompanySerializer()
    user_type = users_serializers.CompanyTypeSerializer()
    # files = files_serializers.f()

    class Meta:
        model = models.Carrier
        fields = "__all__"

        read_only_fields = [
            "company",
            "user_type",
        ]

class DiscountRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiscountRate
        fields = "__all__"


class CompanyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyFile
        fields = "__all__"


class CompanyInvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyInvite
        fields = "__all__"

        # extra_kwargs = {
        #     "email": {
        #         "validators": [UniqueValidator(queryset=models.CompanyInvite.objects.filter(connected=False))]
        #     }
        # }


    def create(self, validated_data):
        user = self.context["user"]
        billing_comapny = user.company
        validated_data["company"] = billing_comapny
        validated_data["user"] = self.context["user"]
        # invitee = models.CompanyInvite.objects.get()
        invited_user = models.CompanyInvite.objects.create(**validated_data)
        token = jwt.encode({"exp": datetime.now(tz=timezone.utc)+ timedelta(minutes=50), "id":str(invited_user.id), "email":invited_user.email}, "secret", algorithm="HS256")
        invited_user.token = token
        invited_user.save()
        # current_site = get_current_site(request).domain
        current_site = config("CURRENT_SITE")
        relative_link = reverse("invite-accept")
        abs_url = f"{current_site}{relative_link}?token={token}"
        email_body = (
            "Hello\t"
            # + validated_data["email"]
            + "\n "
            + "You have been invited to POD by "
            + user.email
            + "\nclink the link below to activate your account\n"
            + abs_url
        )
        data = {
            "email_body": email_body,
            "email_subject": "Verify your email",
            "to_email": validated_data["email"],
        }
        Util.send_email(data)
        return invited_user


    def to_representation(self, instance):
        data = super(CompanyInvitesSerializer, self).to_representation(instance)
        data["role"] = instance.role.name
        data["reporting_to"] = instance.reporting_to.name
        user = User.objects.filter(email =data["email"]).values_list("is_active",flat=True)
        if user:
            data["active"]=user[0]
            return data
        data["active"]=False
        return data

class InvitesConnectedSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True
    )
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True
    )
    email = serializers.EmailField(required=True)
    company = serializers.CharField(max_length=255)
    def save(self):
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]
        company = self.validated_data["company"]
        company = Company.objects.get(id=company)
        # check for confirm password match
        if password != confirm_password:
            raise serializers.ValidationError({"message": "Passwords doesn t match."})
        else:
            hash_password = make_password(self.validated_data["password"])
            register = models.User(
                email=self.validated_data["email"],
                password=hash_password,
                company=company,
                is_active=True
            )
            register.save()
        return register



    def validate_password(self, password):
        min_length = 8
        if len(password) < min_length:
            raise serializers.ValidationError(
                {
                    "message": "Password must be at least %s characters long."
                    % (str(min_length))
                }
            )
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            raise serializers.ValidationError(
                {"message": "Password must contain at least 1 uppercase letter."}
            )
        # check for lowercase letter
        elif not any(c.islower() for c in password):
            raise serializers.ValidationError(
                {"message": "Password must contain at least 1 lowercase letter."}
            )
        # check for digit
        elif sum(c.isdigit() for c in password) < 1:
            raise serializers.ValidationError(
                {"message": "Password must contain at least 1 number."}
            )
        else:
            return password

