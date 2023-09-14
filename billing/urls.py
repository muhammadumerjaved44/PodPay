from django.urls import path
from billing.views import BillingView

urlpatterns = [
    path("billing/", BillingView.as_view(), name="billing"),
    path("billing/<str:pk>", BillingView.as_view(), name="billing"),
]
