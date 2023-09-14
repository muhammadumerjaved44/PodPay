from django.db import models
from .watermark import watermark_text
import uuid

# create contact us model
class Contact(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class SectionType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section_name = models.CharField(max_length=20)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="icon")
    description = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    page_type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.section_name


# create Section us model
class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section_type = models.ForeignKey(
        SectionType, on_delete=models.CASCADE, related_name="section", null=True
    )
    image = models.ImageField(null=True, blank=True, upload_to="icon")
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    class_icon = models.CharField(max_length=50, null=True, blank=True)
    seo_meta_tags = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create model for pod image and invoice and bol
class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pod = models.ImageField(null=True)
    invoice = models.ImageField(null=True, blank=True)
    bol = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ Save method used for saving image fields after inserting uuid watermark on image
        """
        image_list = [self.pod, self.invoice, self.bol]
        self.pod, self.invoice, self.bol = watermark_text(
            image_list, text=self.id, pos=(0, 0)
        )
        super(Document, self).save(*args, **kwargs)


class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class FAQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class Footer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

class FooterLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE,
                              related_name="footer_links", blank=True, null=True
                              )
    def __str__(self):
        return str(self.name) or ' '


class WebinarRegistration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=False)
    email = models.EmailField(max_length=150, blank=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=255, null=True)

    def __str__(self):
        return "%d %s %s" % (self.id,self.full_name, self.email)