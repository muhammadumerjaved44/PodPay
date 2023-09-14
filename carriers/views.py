from rest_framework.views import APIView
from rest_framework.response import Response
import carriers.serializers as serializers
from rest_framework import status
import carriers.models as models
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.schemas.openapi import AutoSchema
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from users.utils import Util
from users.models import User
from django.contrib.auth.hashers import make_password
import jwt
from django.utils import timezone
from datetime import datetime, timedelta
from decouple import config
from caseconverter import pascalcase
class CarrierView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Carrier.objects.all()
            serializer = serializers.CarrierSerializers(instance, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.Carrier, id=pk)
        serializer = serializers.CarrierSerializers(instance)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(serializer = serializers.CarrierSerializers)
    def post(self, request, format=None):
        serializer = serializers.CarrierSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    @swagger_auto_schema(serializer = serializers.CarrierSerializers)
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.Carrier, id=pk)
        serializer = serializers.CarrierSerializers(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(serializer = serializers.CarrierSerializers)
    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.Carrier, id=pk)
        serializer = serializers.CarrierSerializers(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(serializer = serializers.CarrierSerializers)
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.Carrier, id=pk)
        instance.delete()
        return Response(
            {"message": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

class DiscountRateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = models.DiscountRate.objects.all()
            serializer = serializers.DiscountRateSerializer(data)
            return Response({"status": "success", "data": serializer.data})
        else:
            data = get_object_or_404(models.DiscountRate, id=pk)
            serializer = serializers.DiscountRateSerializer(data)
            return Response({"status": "success", "data": serializer.data})

    # Create Instance for document
    def post(self, request, format=None):
        serializer = serializers.DiscountRateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = get_object_or_404(models.DiscountRate, id=pk)
        serializer = serializers.DiscountRateSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.DiscountRate, id=pk)
        instance.delete()
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

class CompanyFileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = models.CompanyFile.objects.all()
            serializer = serializers.CompanyFileSerializer(data)
            return Response({"status": "success", "data": serializer.data})
        else:
            data = get_object_or_404(models.CompanyFile, id=pk)
            serializer = serializers.CompanyFileSerializer(data)
            return Response({"status": "success", "data": serializer.data})

    # Create Instance for document
    def post(self, request, format=None):
        file_type = request.GET.get("file_type")
        company = request.user.company
        request.data["user"]=request.user.id
        request.data["company"]=company.id
        request.data["file_type"]=file_type
        serializer = serializers.CompanyFileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        company = request.user.company
        request.data["user"]=request.user.id
        request.data["company"]=company.id
        data = get_object_or_404(models.CompanyFile, id=pk)
        serializer = serializers.CompanyFileSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Update Document Instance
    def patch(self, request, pk, format=None):
        company = request.user.company
        request.data["user"]=request.user.id
        request.data["company"]=company.id
        data = get_object_or_404(models.CompanyFile, id=pk)
        serializer = serializers.CompanyFileSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class CompanyInvitesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None, format=None):
        connected_user = request.GET.get("connected")
        connected_user = pascalcase(connected_user)
        # if connected_user == "true":
        #     connected_user = True
        if pk is None:
            data = models.CompanyInvite.objects.filter(user=request.user.id, connected=connected_user)
            serializer = serializers.CompanyInvitesSerializer(data, many=True)

            return Response({"status": "success", "data": serializer.data})

        else:
            data = get_object_or_404(models.CompanyInvite, id=pk)
            serializer = serializers.CompanyInvitesSerializer(data)
            return Response({"status": "success", "data": serializer.data})

    # Create Instance for document
    def post(self, request, format=None):

        serializer = serializers.CompanyInvitesSerializer(data=request.data, context={"user": request.user}, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = get_object_or_404(models.CompanyInvite, id=pk)
        serializer = serializers.CompanyInvitesSerializer(data, data=request.data, context={"user": request.user}, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Update Document Instance
    def patch(self, request, pk, format=None):
        data = get_object_or_404(models.CompanyInvite, id=pk)
        token = jwt.encode({"exp": datetime.now(tz=timezone.utc)+ timedelta(minutes=50), "id":str(data.id), "email":data.email}, "secret", algorithm="HS256")
        request.data["token"] = token
        serializer = serializers.CompanyInvitesSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            current_site = config("CURRENT_SITE")
            relative_link = reverse("invite-accept")
            abs_url = f"{current_site}{relative_link}?token={token}"
            email_body = (
                "Hello\t"
                # + validated_data["email"]
                + "\n "
                + "You have been invited to POD by "
                + request.user.email
                + "\nclink the link below to activate your account\n"
                + abs_url
            )
            data = {
                "email_body": email_body,
                "email_subject": "Verify your email",
                "to_email": serializer.data["email"],
            }
            Util.send_email(data)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": "serializer.errors"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk=None, format=None):
            instance = get_object_or_404(models.CompanyInvite, id=pk)
            instance.delete()
            try:
                user = User.objects.get(email=instance.email)
                user.delete()
                return Response(
                    {"message": "Connection deleted successfully"}, status=status.HTTP_200_OK
                )
            except:
                return Response(
                    {"message": "Invitee deleted successfully"}, status=status.HTTP_200_OK
                )
            # # if user:

            # return Response(
            #     {"message": "Invitee deleted successfully"}, status=status.HTTP_204_NO_CONTENT
            # )


class InvitesConnectedView(APIView):
    def get(self, request, format=None):
        encoded_jwt = request.GET.get("token")
        try:
            decoded_data = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
            invite_id = decoded_data["id"]
            invite_email = decoded_data["email"]
            invited_user = models.CompanyInvite.objects.get(id=invite_id)

            return Response(
                {"success": "Valid Token"},
                status=status.HTTP_200_OK,
            )

        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        encoded_jwt = request.GET.get("token")
        try:
            decoded_data = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
            invite_id = decoded_data["id"]
            invite_email = decoded_data["email"]
            invited_user = models.CompanyInvite.objects.get(id=invite_id)
            invited_user.connected = True
            invited_user.save()
            request.data["email"] = invited_user.email
            request.data["company"] = str(invited_user.company.id)#.values_list("id", flat=True)
            serializer = serializers.InvitesConnectedSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"success": "Successfully activated user account","data": serializer.data},
                    status=status.HTTP_200_OK,
                )
        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )