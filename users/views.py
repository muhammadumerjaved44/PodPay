import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.utils import swagger_auto_schema
from decouple import config
import users.models as models
import users.serializers as serializers
from .utils import Util


class SignUpView(APIView):
    def post(self, request, format=None):
        serializer = serializers.SignUpCustomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_account = serializer.data
            user = models.User.objects.get(email=user_account["email"])
            token = str(RefreshToken.for_user(user).access_token)
            # current_site = get_current_site(request).domain
            current_site = config("CURRENT_SITE")
            relative_link = reverse("email-verify")
            abs_url = f"{current_site}{relative_link}?token={token}"
            email_body = (
                "Hello\t"
                + user.username
                + "\n Click the link below to verify your email \n"
                + "  "
                + abs_url
            )
            data = {
                "email_body": email_body,
                "email_subject": "Verify your email",
                "to_email": user.email,
            }
            Util.send_email(data)

            return Response(
            {
                "message": f'An activation link has been sent to {user_account["email"]}',
            },
            status=status.HTTP_205_RESET_CONTENT,
        )

        else:
            Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST,)
        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView):
    def get(self, request, format=None):
        token = request.GET.get("token")
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256",])
            user_id = decoded_data["user_id"]
            user = models.User.objects.get(id=user_id)
            user.is_active = True
            user.save()
            return Response(
                {"success": "Successfully activated user account"},
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


class CustomTokenObtainPairView(TokenObtainPairView):
    parser_classes = (JSONParser,)
    serializer_class = serializers.MyTokenObtainPairSerializer



class CustomTokenRefreshView(TokenRefreshView):
    parser_classes = (JSONParser,)
    serializer_class = serializers.MyTokenObtainPairSerializer



class CompanyView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Company.objects.all()
            serializer = serializers.CompanySerializer(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.Company, id=pk)
        serializer = serializers.CompanySerializer(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # type = request.data["type"]
        # company_type = models.CompanyType.objects.filter(name=type).values_list("id",flat=True)[0]
        # request.data["company_type"]=company_type
        serializer = serializers.CompanySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Update Section Instance
    def patch(self, request, pk, format=None):
        type = request.data["type"]
        company_type = models.CompanyType.objects.filter(name=type).values_list("id",flat=True)[0]
        request.data["company_type"]=company_type
        instance = models.Company.objects.get(pk=pk)
        serializer = serializers.CompanySerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        type = request.data["type"]
        company_type = models.CompanyType.objects.filter(name=type).values_list("id",flat=True)[0]
        request.data["company_type"]=company_type
        instance = models.Company.objects.get(pk=pk)
        serializer = serializers.CompanySerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        instance = models.Company.objects.get(pk=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.UserProfile.objects.all()
            serializer = serializers.UserProfileSerializer(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.UserProfile, id=pk)
        serializer = serializers.UserProfileSerializer(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.UserProfile, id=pk)
        serializer = serializers.UserProfileSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.UserProfile, id=pk)
        serializer = serializers.UserProfileSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.UserProfile, id=pk)
        instance.delete()
        return Response(
            {"stauts": "success", "data": f"Profile id={pk} deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class ChnagePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None, format=None):
        user_obj = models.User.objects.get(email=request.user)
        if check_password(request.data["old_password"], user_obj.password):
            serializer = serializers.ChangePasswordSerializer(data=request.data)
            if serializer.is_valid():
                user_obj.set_password(serializer.data["password"])
                user_obj.save()
                return Response(
                    {"stauts": "success", "data": f"Updated Password"}, status=status.HTTP_200_OK
                )
            return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"stauts": "success", "data": f"Incorrect Password"}, status=status.HTTP_403_FORBIDDEN
            )


class ResetPasswordView(APIView):

    def post(self, request, format=None):
        try:
            user = models.User.objects.get(email=request.data["email"])
            token = str(RefreshToken.for_user(user).access_token)
            # current_site = get_current_site(request).domain
            current_site = config("CURRENT_SITE")
            relative_link = reverse("password-reset-done")
            abs_url = f"{current_site}{relative_link}?token={token}"

            email_body = (
                "Hello\t"
                + user.username
                + "\n Click the link below to reset your password \n"
                + abs_url+ " "
            )
            data = {
                "email_body": email_body,
                "email_subject": "Reset your password",
                "to_email": user.email,
            }
            Util.send_email(data)
            # return Response(
            #     {
            #         "message": f"A password activation link has been sent an email to {user.email}"
            #     },
            #     status=status.HTTP_205_RESET_CONTENT,
            # )
            return Response(
                data,
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            return Response(
                {"message": "Email not registered"}, status=status.HTTP_404_NOT_FOUND
            )

class ResetPasswordDoneView(APIView):

    def put(self, request):
        token = request.GET.get("token")
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256",])
            user_id = decoded_data["user_id"]
            user = models.User.objects.get(id=user_id)
            serializer = serializers.PasswordResetSerializer(data=request.data)
            if serializer.is_valid():
                user.set_password(serializer.data["password"])
                user.save()
                return Response(
                    {"success": "Your password has been reset successfully",},
                    status=status.HTTP_200_OK
                )
        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"stauts": "error", "data": f"Reset link expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"stauts": "error", "data": f"Invalid token"}, status=status.HTTP_400_BAD_REQUEST
                )


class CheckEmailExistsView(APIView):
    @swagger_auto_schema(request_body=serializers.CheckEmailExistsSerializer)
    def post(self, request, format=None):
        serializer = serializers.CheckEmailExistsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                    {"stauts": "success", "data":"You can set this email"},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"stauts": "error", "data": f"Email is already exsist"}, status=status.HTTP_409_CONFLICT
            )

class UserRoleView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = models.UserRole.objects.all()
            serializer = serializers.UserRoleSerializer(data, many=True)
            return Response({"stauts": "success", "data": serializer.data})
        data = get_object_or_404(models.UserRole, id=pk)
        serializer = serializers.UserRoleSerializer(data, many=True)
        return Response({"stauts": "success", "data": serializer.data})

    def post(self, request, format=None):
        serializer = serializers.UserRoleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserUpdateView(APIView):

    def patch(self, request, format=None):
        print(request.data)
        user = get_object_or_404(models.User, email=request.data["email"])
        print("user", user)
        # return Response({"message": "successfully changed", "status":user.is_active}, status=status.HTTP_200_OK)
        serializer = serializers.UserUpdateSerializer(
            instance=user, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "successfully changed", "data":serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)