from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ContactSerializer,
    SectionSerializer,
    SectionTypeSerializer,
    DocumentSerializer,
    QuoteSerializer,
    FAQSerializer,
    FooterLinkSerializer,
    FooterSerializer,
    WebinarSerializer
)
from rest_framework import status
from .models import Section, SectionType, Document, Contact, Quote, FAQ, Footer, FooterLink, WebinarRegistration
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from users.utils import Util


# Contact form view
class ContactView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = Contact.objects.all()
            serializer = ContactSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        instance = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(instance)
        return Response(
            {"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

        # Update Section Instance

    def patch(self, request, pk, format=None):
        instance = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        instance = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(Contact, id=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


# Section  view
class SectionView(APIView):
    def get(self, request, pk=None, format=None):

        if pk is None:
            data = Section.objects.all()
            serializer = SectionSerializer(data, many=True)
            return Response({"stauts": "success", "data": serializer.data})

        data = Section.objects.get(pk=pk)
        serializer = SectionSerializer(data)
        return Response({"stauts": "success", "data": serializer.data})

        # Create Instance for document

    def post(self, request, format=None):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = Section.objects.get(pk=pk)
        serializer = SectionSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk, format=None):
        data = Section.objects.get(pk=pk)
        serializer = SectionSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Section Type View
class FooterView(APIView):
    def get(self, request, pk=None, format=None):
        footer_name = request.GET.get("name")
        if footer_name is None:
            data = Footer.objects.all()#.values_list("name", flat=True)
            # print(data)
            serializer = FooterSerializer(data, many=True)
            footerdata = {}
            for data in serializer.data:
                footerdata[(data["name"])] = data
            return Response({"stauts": "success", "data": footerdata})
        data = Footer.objects.filter(name=footer_name)
        serializer = FooterSerializer(data, many=True)
        return Response({"stauts": "success", "data": serializer.data})

    def post(self, request, format=None):
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = get_object_or_404(Footer, id=pk)
        serializer = FooterSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk, format=None):
        data = get_object_or_404(Footer, id=pk)
        serializer = FooterSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Document view
class DocumentView(APIView):

    # Retrieve Document
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = Document.objects.all()
            serializer = DocumentSerializer(data)
            return Response({"stauts": "success", "data": serializer.data})
        else:
            data = get_object_or_404(Document, id=pk)
            serializer = DocumentSerializer(data)
            return Response({"stauts": "success", "data": serializer.data})

    # Create Instance for document
    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = get_object_or_404(Document, id=pk)
        serializer = DocumentSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Update Document Instance
    def patch(self, request, pk, format=None):
        data = get_object_or_404(Document, id=pk)
        serializer = DocumentSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Get a Quote view
class QuoteView(APIView):

    # Retrieve Quotes
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = Quote.objects.all()
            serializer = QuoteSerializer(data, many=True)
            return Response({"stauts": "success", "data": serializer.data})
        else:
            data = get_object_or_404(Quote, id=pk)
            serializer = QuoteSerializer(data)
            return Response({"stauts": "success", "data": serializer.data})

    # Create Instance for Quote
    def post(self, request, format=None):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class FAQView(APIView):

    # Retrieve FAQs
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = FAQ.objects.all()
            serializer = FAQSerializer(data, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        if pk == "0":
            data = FAQ.objects.all().order_by("id")[:4]
            serializer = FAQSerializer(data, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        elif pk == "1":
            data = FAQ.objects.all().order_by("id")[4:8]
            serializer = FAQSerializer(data, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    # Create Instance for FAQs
    def post(self, request, format=None):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Update Instance for document
    def put(self, request, pk, format=None):
        data = FAQ.objects.get(pk=pk)
        serializer = FAQSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Partial Update Instance for document
    def patch(self, request, pk, format=None):
        data = FAQ.objects.get(pk=pk)
        serializer = FAQSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class SectionTypeView(APIView):
    def get(self, request, pk=None, format=None):
        section_name = request.GET.get("name")
        page_type = request.GET.get("page_type")
        if section_name is None:
            data = SectionType.objects.filter(page_type = page_type).values_list("section_name", flat=True)
            # serializer = SectionTypeSerializer(data, many=True)
            return Response({"stauts": "success", "data": data})
        data = SectionType.objects.filter(section_name=section_name, page_type=page_type)
        serializer = SectionTypeSerializer(data, many=True)
        return Response({"stauts": "success", "data": serializer.data})

    def post(self, request, format=None):
        serializer = SectionTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = get_object_or_404(SectionType, id=pk)
        serializer = SectionTypeSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk, format=None):
        data = get_object_or_404(SectionType, id=pk)
        serializer = SectionTypeSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class WebinarRegistrationView(APIView):

    # Retrieve Registration data
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = WebinarRegistration.objects.all()
            print("data", data)
            serializer = WebinarSerializer(data, many=True)
            return Response({"stauts": "success", "data": serializer.data})
        else:
            data = get_object_or_404(WebinarRegistration, id=pk)
            serializer = WebinarSerializer(data)
            return Response({"stauts": "success", "data": serializer.data})

    # Create Instance for WebinarRegistration
    def post(self, request, format=None):
        if request.data["industry"] is None:
            request.data["industry"] = request.data["other"]
        serializer = WebinarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            email_body = (
                "Hello\t"
                + request.data["full_name"]
                + "\n You have successfully registered for Webinar \n"
                + "  "
            )
            data = {
                "email_body": email_body,
                "email_subject": "Verify your email",
                "to_email": request.data["email"]
            }
            Util.send_email(data)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        data = get_object_or_404(WebinarRegistration, id=pk)
        serializer = WebinarSerializer(data, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Update WebinarRegistration Instance
    def patch(self, request, pk, format=None):
        data = get_object_or_404(WebinarRegistration, id=pk)
        serializer = WebinarSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )