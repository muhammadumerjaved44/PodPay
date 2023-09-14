from django.contrib import admin
import carriers.models as models
from django_paranoid.admin import ParanoidAdmin
@admin.register(models.CarrierFiles)
class CarrierFilesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.CarrierFiles._meta.fields]
    list_filter = list_display





@admin.register(models.Carrier)
class CarrierCompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Carrier._meta.fields]
    list_filter = list_display


@admin.register(models.DiscountRate)
class DiscountRateAdmin(admin.ModelAdmin,):
    list_display = ["id", "discount_rate", "percentage"]

@admin.register(models.CompanyFile)
class CompanyFilesAdmin(admin.ModelAdmin,):
    list_display = ["id", "file", "file_type", "user", "company"]

@admin.register(models.CompanyInvite)
class CompanyInvitesAdmin(ParanoidAdmin):
    list_display = ["id", "user", "company", "email", "role", "reporting_to", "connected"]
# admin.site.register(models.CompanyInvites, admin.ModelAdmin)