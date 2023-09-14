from rest_framework import serializers
from billing.models import Billing


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["user"]
        billing_comapny = user.company
        validated_data["company"] = billing_comapny
        validated_data["user"] = self.context["user"]
        billing = Billing.objects.create(**validated_data)
        return billing
