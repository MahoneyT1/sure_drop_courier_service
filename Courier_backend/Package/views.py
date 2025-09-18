"""
    This module contains the views for the Package app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Package objects.
    It uses Django REST Framework's concrete generic to handle the requests
    and responses.
    The views are designed to be used with the PackageSerializer class
    to serialize and deserialize Package objects.
    The views also include authentication and permission classes
    to ensure that only authorized users can access the endpoints.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Package.models import Package
from Package.serializer import PackageSerializer
from Courier.models import Courier
from Courier.serializer import CourierSerializer
from Delivery.models import Delivery
from Delivery.serializer import DeliverySerializer
from Receipt.models import Receipt
from Receipt.serializer import ReceiptSerializer
from DeliveryStatusHistory.models import DeliveryStatusHistory
from DeliveryStatusHistory.serializer import DeliveryStatusHistorySerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils import timezone
import datetime
import traceback


class PackageListCreateView(ListCreateAPIView):
    """
        Api view for listing and creating Package objects.
        It uses the PackageSerializer class to serialize and deserialize
        Package objects.
    """

    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        """
            Handle GET requests to list all Package objects.
        """
        print("get list of package worked, but not cache")
        packages = self.get_queryset()
        serializer = self.get_serializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
            Handle POST requests to create a new Package object.
        """
        # create a package
        serializer = PackageSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        package = serializer.save()

        return Response(
            PackageSerializer(
                package, 
                context={'request': request}).data, 
                status=status.HTTP_201_CREATED
            )
       

class PackageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        Api view for retrieving, updating, and deleting Package objects.
        It uses the PackageSerializer class to serialize and deserialize
        Package objects.
    """

    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Package.objects.prefetch_related(
            Prefetch(
                'deliveries', 
                queryset=Delivery.objects.select_related(
                    'courier').prefetch_related(
                        'histories'), 
            ),
        ).select_related('user','receipt')

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Package.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        """
            Handle PUT requests to update a specific Package object.
        """
        package = self.get_object()
        serializer = self.get_serializer(package, data=request.data)
        serializer.is_valid(raise_exception=True)
        package = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
            Handle DELETE requests to delete a specific Package object.
        """
        package = self.get_object()
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
