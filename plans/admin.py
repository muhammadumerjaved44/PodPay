from django.contrib import admin
import plans.models as models
import plans.admin_forms as forms
import pandas as pd
import numpy as np


@admin.register(models.PlanRoleCategory)
class PlanRoleCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.PlanRoleCategory._meta.fields]
    list_filter = list_display


@admin.register(models.PlanDateType)
class PlanDateTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.PlanDateType._meta.fields]
    list_filter = list_display

@admin.register(models.PlansFeaturesCategory)
class PlansFeaturesCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.PlansFeaturesCategory._meta.fields]
    list_filter = list_display



@admin.register(models.PlansFeatures)
class AllPlansAdmin(admin.ModelAdmin):

    form = forms.PlansFeaturesAdminForm
    #
    list_display = [field.name for field in models.PlansFeatures._meta.get_fields()]
    list_filter = list_display


@admin.register(models.PlansFromFile)
class PlansUploadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.PlansFromFile._meta.get_fields()]


    def update_rol_category_date(self, role, category, date):
        role_obj, created = models.PlanRoleCategory.objects.update_or_create(name=role)
        features_obj, created = models.PlansFeaturesCategory.objects.update_or_create(name=category)
        date_obj, created = models.PlanDateType.objects.update_or_create(name=date)

        return role_obj, features_obj, date_obj

    def process_csv(self, file):
        df = pd.read_excel(file)
        df = df.replace("P", 1).replace("x", 2).replace(np.nan, 0)
        features = df.columns.to_list()
        features.remove('features')
        for col in features:
            role, category, date = col.split('_')
            role_obj, features_obj, date_obj = self.update_rol_category_date(role, category, date)
            temp_dict = {}
            for i, v in zip(df['features'], df[col]):
                temp_dict.update({i: v})

            models.PlansFeatures.objects.update_or_create(
                name=col,
                **temp_dict,
                plan_date_type=date_obj,
                plan_role_category=role_obj,
                plan_features_category=features_obj
            )

    def save_model(self, request, obj, form, change):
        #     CHOICES = (
        #     (0, 'N/A'),
        #     (1, 'Not Applicable'),
        #     (2, 'Applicable'),
        # )
        self.process_csv(request.FILES["file"])

        return super().save_model(request, obj, form, change)
