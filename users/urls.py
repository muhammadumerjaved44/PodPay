from django.conf.urls import include
from django.urls import path, re_path
import rest_framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# from users.temp_views import APILoginViewSet, APILogoutViewSet, APITokenViewSet, APIUserInfoViewSet
from users import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="sign-up"),
    # path("signup/<str:pk>", views.SignUpView.as_view(), name="sign-up"),
    path("user-status/", views.UserUpdateView.as_view(), name="user-status"),
    path("login/", views.CustomTokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("login/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("email-exist/", views.CheckEmailExistsView.as_view(), name="email-exist"),
    path("email-verify/", views.VerifyEmail.as_view(), name="email-verify"),
    path(
        "password/chnage-password/",
        views.ChnagePasswordView.as_view(),
        name="chnage-password",
    ),
    path(
        "password/password-reset/",
        views.ResetPasswordView.as_view(),
        name="password-reset",
    ),
    path(
        "password/password-reset-done/",
        views.ResetPasswordDoneView.as_view(),
        name="password-reset-done",
    ),

    path("companies/", views.CompanyView.as_view()),
    path("companies/<str:pk>", views.CompanyView.as_view()),
    path("profiles/", views.UserProfileView.as_view()),
    path("profiles/<str:pk>", views.UserProfileView.as_view()),
    path("user-role/", views.UserRoleView.as_view(), name="user-role"),
    path("user-role/<str:pk>", views.UserRoleView.as_view, name="user-role")
]
