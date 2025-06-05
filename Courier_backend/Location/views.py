""" location/views.py
    Handles all views
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Location.models import Location
from Location.serializer import LocationSerializer


class LocationListCreateView(ListCreateAPIView):
    """
        handles creation of location object and listin as well
    """

    queryset = Location.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        """
            List all Location objects
        """
        locations = self.get_queryset()
        serializer = self.get_serializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
            creates a location object
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class LocationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        handles retrieval, update and deletion of location object
    """

    def get(self, request, *args, **kwargs):
        """
            Retrieve a specific Location object
        """
        location = self.get_object()
        serializer = self.get_serializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        """
            updates a location object
        """
        location = self.get_object()
        serializer = self.get_serializer(location, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        """deletes an object"""

        object_to_del = self.get_object()
        object_to_del.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
