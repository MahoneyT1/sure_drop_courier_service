"""
# Delivery/views.py
This module contains the views for the Delivery app.
It defines the API endpoints for creating, retrieving, updating,
and deleting Delivery objects.
It uses Django REST Framework's concrete generic to handle the requests
and responses.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Delivery.models import Delivery
from Delivery.serializer import DeliverySerializer


class DeliveryListCreateView(ListCreateAPIView):
    """
    Api view for listing and creating Delivery objects.
    It uses the DeliverySerializer class to serialize and deserialize
    Delivery objects.
    """

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list all Delivery objects.
        """
        deliveries = self.get_queryset()
        serializer = self.get_serializer(deliveries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new Delivery object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeliveryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Api view for retrieving, updating, and deleting Delivery objects.
    It uses the DeliverySerializer class to serialize and deserialize
    Delivery objects.
    """

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a specific Delivery object.
        """
        delivery = self.get_object()
        serializer = self.get_serializer(delivery)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a specific Delivery object.
        """
        delivery = self.get_object()
        serializer = self.get_serializer(delivery, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a specific Delivery object.
        """
        delivery = self.get_object()
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    