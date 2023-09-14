
from files.models import Files
from users.models import Company
from django.db import models
from users.models import  User, Company, CompanyType
from django.utils.translation import gettext_lazy as _
import uuid
from users.models import UserRole
from django_paranoid.models import ParanoidModel

class CarrierFiles(Files):
    pass


class Carrier(models.Model):
    dot = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    user_type = models.ForeignKey(CompanyType, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    files = models.ForeignKey(CarrierFiles, on_delete=models.CASCADE)


class DiscountRate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount_rate  = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%d %s %s" % (self.id, self.discount_rate, self.percentage)

class CompanyFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="files", null=True, blank=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        User,
        related_name="company_user",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    company = models.ForeignKey(Company,
                                     related_name="company_files",
                                     blank=True,
                                     null=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return "%d %s" % (self.id,self.file_type)


class CompanyInvite(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        related_name="user_invites",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    company = models.ForeignKey(Company,
                                     related_name="company_invites",
                                     blank=True,
                                     null=True,
                                     on_delete=models.SET_NULL)
    email = models.EmailField(_("email"))
    role = models.ForeignKey(UserRole,
                                     related_name="invitee_role",
                                     blank=True,
                                     null=True,
                                     on_delete=models.SET_NULL)
    reporting_to = models.ForeignKey(UserRole,
                                     related_name="reporting_role",
                                     blank=True,
                                     null=True,
                                     on_delete=models.SET_NULL)
    connected = models.BooleanField(default=False)
    token = models.CharField(_("token"), max_length=255, default=False)
    def __str__(self):
        return "%d %s" % (self.id, self.email)
