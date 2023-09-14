from django.urls import path
from .views import (
    ContactView,
    SectionView,
    SectionTypeView,
    DocumentView,
    QuoteView,
    FAQView,
    FooterView,
    WebinarRegistrationView
)

urlpatterns = [
    path("contact-us", ContactView.as_view(), name="contact-us"),
    path("contact-us/<str:pk>", ContactView.as_view(), name="contact-us"),
    path("section", SectionView.as_view(), name="section"),
    path("section/<str:pk>", SectionView.as_view(), name="section"),
    path("section-type/", SectionTypeView.as_view(), name="section-type"),
    path("section-type/<str:pk>", SectionTypeView.as_view(), name="section-type"),
    path("document", DocumentView.as_view(), name="document"),
    path("document/<str:pk>", DocumentView.as_view(), name="document"),
    path("request-quote/", QuoteView.as_view(), name="request-quote"),
    path("faq", FAQView.as_view(), name="faq"),
    path("faq/<str:pk>", FAQView.as_view(), name="faq"),
    path("footer/", FooterView.as_view(), name="footer"),
    path("webinar/", WebinarRegistrationView.as_view(), name="webinar"),
    path("webinar/<str:pk>", WebinarRegistrationView.as_view(), name="webinar")
]

