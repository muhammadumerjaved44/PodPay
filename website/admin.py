from django.contrib import admin
from .models import Contact, Section, Document, SectionType, Quote, FAQ, Footer, FooterLink, WebinarRegistration

# Register Contact Model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "company_name", "phone", "comments")


#  Register Section Model
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "description", "seo_meta_tags", "is_visible")


#  Register Document Model
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "pod", "invoice", "bol")


#   Register Section Type Model
@admin.register(SectionType)
class SectionTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "section_name", "title", "description", "description2", "page_type")


# Register QUote Model
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "company_name", "phone", "comments")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer")


admin.site.register(Footer, admin.ModelAdmin)
admin.site.register(FooterLink, admin.ModelAdmin)
admin.site.register(WebinarRegistration, admin.ModelAdmin)