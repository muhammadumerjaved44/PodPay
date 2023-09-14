from django.shortcuts import render
from rest_framework.views import APIView
from billing.serializers import BillingSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Billing
from rest_framework.response import Response

# Create your views here.

class BillingView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = Billing.objects.all()
            serializer = BillingSerializer(instance, many=True)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        instance = get_object_or_404(Billing, id=pk)
        serializer = BillingSerializer(instance)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        serializer = BillingSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

        # Update Section Instance

    def patch(self, request, pk, format=None):
        instance = get_object_or_404(Billing, id=pk)
        serializer = BillingSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk, format=None):
        instance = get_object_or_404(Billing, id=pk)
        serializer = BillingSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(Billing, id=pk)
        instance.delete()
        return Response(
            {"message": "Billing deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
