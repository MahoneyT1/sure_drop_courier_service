"""
    location URL Configuration
    This module contains the URL patterns for the Location app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Location objects.
"""

from django.urls import path
from Location.views import (
    LocationListCreateView,
    LocationRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDestroyView.as_view(), name='location-retrieve-update-destroy'),
]
