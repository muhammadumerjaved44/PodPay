from django.urls import path
import plans.views as views


urlpatterns = [
    path("plans/", views.PlansFeaturesView.as_view(), name="plans"),
    path("plans/<str:pk>", views.PlansFeaturesView.as_view(), name="plan"),
    path("plans-date-type/", views.PlanDateTypeView.as_view(), name="plans-type"),
    path("plans-date-type/<str:pk>", views.PlanDateTypeView.as_view(), name="plan-type"),
    path("plans-role-category/", views.PlanRoleCategoryView.as_view(), name="plans-category"),
    path("plans-role-category/<str:pk>", views.PlanRoleCategoryView.as_view(), name="plan-category"),
    path("payment-method", views.StripeView.as_view(), name="payment-method"),
    path("stripe-price/", views.StripePrice.as_view(), name="stripe-price")
]
