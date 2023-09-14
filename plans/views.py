import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
import plans.serializers as serializers
from rest_framework import status
import plans.models as models
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.schemas.openapi import AutoSchema
from drf_yasg.utils import swagger_auto_schema
from decouple import config
from drf_stripe.models import Price, Product

stripe.api_key = config("STRIPE_API_SECRET")
class PlanDateTypeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.PlanDateType.objects.all()
            serializer = serializers.PlanDateTypeSerializers(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.PlanDateType, id=pk)
        serializer = serializers.PlanDateTypeSerializers(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.PlanDateTypeSerializers)
    def post(self, request, format=None):
        serializer = serializers.PlanDateTypeSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    @swagger_auto_schema(request_body=serializers.PlanDateTypeSerializers)
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.PlanDateType, id=pk)
        serializer = serializers.PlanDateTypeSerializers(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlanDateTypeSerializers)
    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.PlanDateType, id=pk)
        serializer = serializers.PlanDateTypeSerializers(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlanDateTypeSerializers)
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.PlanDateType, id=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

class PlanRoleCategoryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.PlanRoleCategory.objects.all()
            serializer = serializers.PlanRoleCategorySerializers(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.PlanRoleCategory, id=pk)
        serializer = serializers.PlanRoleCategorySerializers(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.PlanRoleCategorySerializers)
    def post(self, request, format=None):
        serializer = serializers.PlanRoleCategorySerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    @swagger_auto_schema(request_body=serializers.PlanRoleCategorySerializers)
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.PlanRoleCategory, id=pk)
        serializer = serializers.PlanRoleCategorySerializers(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlanRoleCategorySerializers)
    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.PlanRoleCategory, id=pk)
        serializer = serializers.PlanRoleCategorySerializers(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlanRoleCategorySerializers)
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.PlanRoleCategory, id=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

class PlansFeaturesCategoryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.PlansFeaturesCategory.objects.all()
            serializer = serializers.PlansFeaturesCategorySerializers(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.PlansFeaturesCategory, id=pk)
        serializer = serializers.PlansFeaturesCategorySerializers(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.PlansFeaturesCategorySerializers)
    def post(self, request, format=None):
        serializer = serializers.PlansFeaturesCategorySerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    @swagger_auto_schema(request_body=serializers.PlansFeaturesCategorySerializers)
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.PlansFeaturesCategory, id=pk)
        serializer = serializers.PlansFeaturesCategorySerializers(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlansFeaturesCategorySerializers)
    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.PlansFeaturesCategory, id=pk)
        serializer = serializers.PlansFeaturesCategorySerializers(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlansFeaturesCategorySerializers)
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.PlansFeaturesCategory, id=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

class PlansFeaturesView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.PlansFeatures.objects.all()
            serializer = serializers.PlansFeaturesSerializers(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.PlansFeatures, id=pk)
        serializer = serializers.PlansFeaturesSerializers(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.PlansFeaturesSerializers)
    def post(self, request, format=None):
        serializer = serializers.PlansFeaturesSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    @swagger_auto_schema(request_body=serializers.PlansFeaturesSerializers)
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.PlansFeatures, id=pk)
        serializer = serializers.PlansFeaturesSerializers(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlansFeaturesSerializers)
    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.PlansFeatures, id=pk)
        serializer = serializers.PlansFeaturesSerializers(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.PlansFeaturesSerializers)
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.PlansFeatures, id=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class PlansFromFileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.PlansFromFile.objects.all()
            serializer = serializers.PlansFeaturesSerializers(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.PlansFeatures, id=pk)
        serializer = serializers.PlansFeaturesSerializers(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class StripeView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        price_id = request.data["price_id"]
        payment_method = stripe.PaymentMethod.create(
            type=request.data["type"],
            card=request.data["card"],
            billing_details=request.data["billing_details"])
        # customer_data = stripe.Customer.list(email=request.data["billing_details"]["email"]).data

        # if len(customer_data)==0:
        customer = stripe.Customer.create(email=request.data["billing_details"]["email"],
                                          payment_method=payment_method.id,
                                          invoice_settings={
                                            'default_payment_method': payment_method.id
                                        })
        # customer_id = customer.id
        # customer_payment_method = stripe.PaymentMethod.attach(
        #     payment_method.id,
        #     customer=customer_id,
        #     )
        stripe.Subscription.create(customer=customer, items=[
        {
        'price': price_id
        }])
        return Response(payment_method, status=status.HTTP_200_OK)


class StripePrice(APIView):
    def get(self, request, format=None):
        product_type = request.GET.get("product_type")
        price_freq = request.GET.get("price_freq")
        price = Price.objects.filter(product__name=product_type, freq=price_freq).values_list("price_id")[0]
        return Response(price, status=status.HTTP_200_OK)
