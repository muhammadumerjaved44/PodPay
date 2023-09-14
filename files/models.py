from polymorphic.models import PolymorphicModel
from django.db import models
import uuid

class Files(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="files", null=True, blank=True)