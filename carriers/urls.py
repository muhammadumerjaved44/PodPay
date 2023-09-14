from django.urls import path
import carriers.views as views


urlpatterns = [
    path("carriers/", views.CarrierView.as_view(), name="carriers"),
    path("carriers/<str:pk>", views.CarrierView.as_view(), name="carrier"),
    path("discount-rate/", views.DiscountRateView.as_view(), name="discount-rate"),
    path("discount-rate/<str:pk>",views.DiscountRateView.as_view(), name="discount-rate"),
    path("company-files/", views.CompanyFileView.as_view(), name="comapny-files"),
    path("company-files/<str:pk>", views.CompanyFileView.as_view(), name="comapny-files"),
    path("company-invites/", views.CompanyInvitesView.as_view(), name="company-invites"),
    path("company-invites/<str:pk>", views.CompanyInvitesView.as_view(), name="company-invites"),
    path("invite-accept/", views.InvitesConnectedView.as_view(), name="invite-accept"),
    # path("plans-date-type/", views.PlanDateTypeView.as_view(), name="plans-type"),
    # path("plans-date-type/<str:pk>", views.PlanDateTypeView.as_view(), name="plan-type"),
    # path("plans-role-category/", views.PlanRoleCategoryView.as_view(), name="plans-category"),
    # path("plans-role-category/<str:pk>", views.PlanRoleCategoryView.as_view(), name="plan-category")
]
