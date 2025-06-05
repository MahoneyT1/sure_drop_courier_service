"""
    This module contains the views for the Courier app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Courier objects.
    It uses Django REST Framework's concrete generic to handle the requests
    and responses.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Courier.models import Courier
from Courier.serializer import CourierSerializer



class CourierListCreateView(ListCreateAPIView):
    """
        creates and list Courier objects
    """

    queryset = Courier.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CourierSerializer

    def get(self, request, *args, **kwargs):
        """
            List all Courier objects
        """

        couriers = self.get_queryset()
        serializer = self.get_serializer(couriers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
            Create a new Courier object
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CourierRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update, and delete Courier objects
    """

    queryset = Courier.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CourierSerializer

    def get(self, request, *args, **kwargs):
        """
            Retrieve a specific Courier object
        """
        courier = self.get_object()
        serializer = self.get_serializer(courier)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        """
            Update a specific Courier object
        """
        courier = self.get_object()
        serializer = self.get_serializer(courier, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        """
            Delete a specific Courier object
        """
        courier = self.get_object()
        courier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
