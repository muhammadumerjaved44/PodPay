from .models import Contact, Section, Document, SectionType, Quote, FAQ, Footer, FooterLink, WebinarRegistration
from rest_framework import serializers


# contact serializer class
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


# Section serializer class
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


# SectionType serializer class
class SectionTypeSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True, required=False)

    class Meta:
        model = SectionType
        fields = ["id", "section_name", "title", "image", "description", "description2", "section"]


class FooterLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = FooterLink
        fields = ["id", "name", "type"]

    def to_representation(self, instance):
        data = super(FooterLinkSerializer, self).to_representation(instance)
        data[str(instance)] = str(instance)
        return data

class FooterSerializer(serializers.ModelSerializer):
    footer_links = FooterLinkSerializer(many=True, required=False)
    class Meta:
        model = Footer
        fields = ["id", "name", "title", "description", "footer_links"]


# Document serializer class
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

    def update(self, instance, validated_data):
        """using for updating documents images

        Args:
            validated_data (_type_): take validated data from request

        Returns:
            _type_: instance  object
        """
        instance.invoice = validated_data.get("invoice", instance.invoice)
        instance.bol = validated_data.get("bol", instance.bol)
        instance.save()
        return instance


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class WebinarSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebinarRegistration
        fields = "__all__"