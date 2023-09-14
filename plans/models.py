from django.db import models
import uuid
from users.models import User


class PlanDateType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    discription = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class PlanRoleCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    discription = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class PlansFeaturesCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    discription = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class PlansFeatures(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_date_type = models.ForeignKey(
        PlanDateType, related_name="plan_date_type", null=True, on_delete=models.CASCADE
    )
    plan_role_category = models.ForeignKey(
        PlanRoleCategory,
        related_name="plan_role_category",
        null=True,
        on_delete=models.CASCADE,
    )
    plan_features_category = models.ForeignKey(
        PlansFeaturesCategory,
        related_name="plan_features_category",
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, null=True, blank=True, unique=False)
    price = models.CharField(max_length=100, null=True, blank=True)
    members = models.CharField(max_length=100, null=True, blank=True)
    roles = models.CharField(max_length=100, null=True, blank=True)
    pod_upload_limits = models.CharField(max_length=100, null=True, blank=True)
    additional_pod_cost = models.CharField(max_length=100, null=True, blank=True)
    pod_history = models.PositiveSmallIntegerField(null=True, blank=True)
    admin_panel = models.PositiveSmallIntegerField(null=True, blank=True)
    document_storage = models.PositiveSmallIntegerField(null=True, blank=True)
    historical_storage_documents = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    email_support = models.PositiveSmallIntegerField(null=True, blank=True)
    mobile_app = models.PositiveSmallIntegerField(null=True, blank=True)
    multiple_cards_history = models.PositiveSmallIntegerField(null=True, blank=True)
    app_notifications = models.PositiveSmallIntegerField(null=True, blank=True)
    email_notifications = models.PositiveSmallIntegerField(null=True, blank=True)
    members_history = models.PositiveSmallIntegerField(null=True, blank=True)
    dashboard = models.PositiveSmallIntegerField(null=True, blank=True)
    payments_history = models.PositiveSmallIntegerField(null=True, blank=True)
    connections = models.PositiveSmallIntegerField(null=True, blank=True)
    chat_support = models.PositiveSmallIntegerField(null=True, blank=True)
    on_call_support = models.PositiveSmallIntegerField(null=True, blank=True)
    carrier_database = models.PositiveSmallIntegerField(null=True, blank=True)
    broker_database = models.PositiveSmallIntegerField(null=True, blank=True)
    signatories_list = models.PositiveSmallIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class PlansFromFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="icon", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)
