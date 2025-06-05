"""
# Delivery/urls.py
This module contains the URL patterns for the Delivery app.
It defines the API endpoints for creating, retrieving, updating,
and deleting Delivery objects.
"""

from django.urls import path
from Delivery.views import (
    DeliveryListCreateView,
    DeliveryRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('deliveries/', DeliveryListCreateView.as_view(), name='delivery-list-create'),
    path('deliveries/<int:pk>/', DeliveryRetrieveUpdateDestroyView.as_view(), name='delivery-retrieve-update-destroy'),
]
