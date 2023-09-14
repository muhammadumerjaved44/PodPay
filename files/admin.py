from django.contrib import admin
import files.models as models

@admin.register(models.Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Files._meta.fields]
    list_filter = list_display
