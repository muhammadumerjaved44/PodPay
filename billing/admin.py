from django.contrib import admin
from .models import Billing

# Register your models here.


@admin.register(Billing)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "company_name",
        "email",
        "phone_number",
        "country",
        "city",
        "state",
        "street",
        "zip_code",
        "cc_number",
        "cc_expiry",
        "cc_code",
    )

