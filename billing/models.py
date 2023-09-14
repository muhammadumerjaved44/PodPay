from django.db import models
import uuid
from users.models import User,Company
from datetime import datetime
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import gettext as _

# Create your models here.
class Billing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="billing_user",
    )
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True, related_name="billing_company")
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=150)
    cc_number = CardNumberField(_("card number"), max_length=16, default=None)
    cc_expiry = models.CharField(_("expiration date"),max_length=5,default=None)
    cc_code = SecurityCodeField(_("security code"))
    create_date = models.DateTimeField(auto_now_add=True, blank=False)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%d %s %s" % (self.id, self.email, self.phone_number)
