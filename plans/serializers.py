from rest_framework import serializers
import plans.models as models

# contact serializer class
class PlanRoleCategorySerializers(serializers.ModelSerializer):
    """Plans roles category

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model = models.PlanRoleCategory
        fields = "__all__"


# Section serializer class
class PlanDateTypeSerializers(serializers.ModelSerializer):
    """Plans by dates

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = models.PlanDateType
        fields = "__all__"


class PlansFeaturesCategorySerializers(serializers.ModelSerializer):
    """Plans by features

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = models.PlansFeaturesCategory
        fields = "__all__"


class PlansFeaturesSerializers(serializers.ModelSerializer):
    """Plans features

    Args:
        serializers (_type_): _description_
    """

    plan_date_type = PlanDateTypeSerializers()
    plan_role_category = PlanRoleCategorySerializers()
    plan_features_category = PlansFeaturesCategorySerializers()

    class Meta:
        model = models.PlansFeatures
        fields = "__all__"

        read_only_fields = [
            "plan_date_type",
            "plan_role_category",
            "plan_features_category",
        ]
