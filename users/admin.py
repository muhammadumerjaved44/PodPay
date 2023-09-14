from django.contrib import admin
from users.models import User, Company, UserProfile, CompanyType, UserRole
from django.contrib.auth.admin import UserAdmin
from django_paranoid.admin import ParanoidAdmin

@admin.register(Company)
class CompanyAdminView(admin.ModelAdmin):

    list_display = [
        "name",
        "description",
        "MC",
        "DOT",
        "address",
        "address2",
        "zip",
        "city",
        "country",
        # "company_type",
        "phone",
        "is_public",
        "create_date",
        "update_date",
        "created_by"
    ]
    list_filter = list_display

@admin.register(UserProfile)
class UserProfileViewAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "full_name",
        "username",
        "phone",
        "email",
        "zip",
        "city",
        "state",
        "country",
        "create_date",
        "update_date",
    ]
    list_filter = list_display


@admin.register(UserRole)
class UserRoleViewAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(User, UserAdmin,)
admin.site.register(CompanyType, admin.ModelAdmin)

