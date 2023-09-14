from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# import stripe
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(title="My POD API", default_version="0.0.0", description="myPod API "),
    public=True,
)


# customizing admin panel
admin.site.site_header = "Winsport Admin Portal"
admin.site.site_title = "Winsport Admin Portal"
admin.site.index_title = "Welcome to Winsport  Portal"

# Project URLS
urlpatterns = [
    path(
        "docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-schema"
    ),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("", include("website.urls")),
    path("", include("plans.urls")),
    path("", include("carriers.urls")),
    path("", include("billing.urls")),
    path("stripe/", include("drf_stripe.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
