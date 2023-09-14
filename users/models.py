import os
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.template.defaultfilters import slugify

# import code for encoding urls and generating md5 hashes
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import hashlib
from django_paranoid.models import ParanoidModel

try:
    # Python 3.4
    import urllib.parse
except ImportError:
    # Python 2.7
    import urllib

from django.templatetags.static import static
# from django.contrib.auth.models import User as authUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid
from polymorphic.models import PolymorphicModel
from phonenumbers import is_valid_number, parse
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class UserRole(PolymorphicModel):
    USER_TYPES = [
                    ("",'----------'),
                    ("admin", "Admin"),
                    ("manager", "Manager"),
                    ("agent", "Agent"),
                    ("broker", 'Broker'),
                    ("carrier", 'Carrier'),
                    ("financer", 'Financer')
                  ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, choices= USER_TYPES)
    def __str__(self):
        return "%s" % (self.name) or ""
class CompanyType(PolymorphicModel):

    COMPANY_TYPES = [
        ("", '----------'),
        ("broker", 'Broker'),
        ("carrier", 'Carrier'),
        ("financer", 'Financer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=10,
        choices=COMPANY_TYPES,
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

class Company(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)
    MC = models.CharField(max_length=150, blank=True, null=True)
    DOT = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=255)
    address2 = models.CharField(blank=True, null=True, max_length=255)
    zip = models.CharField(blank=True, null=True, max_length=10)
    city = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=100)
    company_type = models.ForeignKey(CompanyType,
                                     related_name="company_type",
                                     blank=True,
                                     null=True,
                                     on_delete=models.SET_NULL)
    phone = models.CharField(blank=True, null=True, max_length=255)
    timezone = models.CharField(blank=True, null=True, max_length=100)
    is_public = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return "%s" % self.name
class User(AbstractUser, ParanoidModel ):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=150, unique=False)
    is_active = models.BooleanField(_("active"), default=False)
    company = models.ForeignKey(Company, related_name="user_company",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,)
    user_role = models.ForeignKey(UserRole, related_name="user_role",
                                  blank=True,
                                  null=True,
                                  on_delete=models.SET_NULL,)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        # if len(self.username) == 0:
        #     return self.is_active
        return self.email


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="userprofiles"
    )
    # birth_date = models.DateField(null=True, blank=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(_("username"), max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    email = models.EmailField(_("email"), blank=True, null=True)
    zip = models.CharField(blank=True, null=True, max_length=10)
    city = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%d %s %s" % (self.user.id, self.user.email, self.phone)



class Files(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

