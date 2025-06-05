"""
    Courier URL Configuration
    This module contains the URL patterns for the Courier app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Courier objects.
    It uses Django REST Framework's concrete generic to handle the requests
    and responses.
"""

from django.urls import path
from Courier.views import (
    CourierListCreateView,
    CourierRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('couriers/', CourierListCreateView.as_view(), name='courier-list-create'),
    path('couriers/<int:pk>/', CourierRetrieveUpdateDestroyView.as_view(), name='courier-retrieve-update-destroy'),
]
