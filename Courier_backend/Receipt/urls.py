"""
    Recept URL Configuration
    This module contains the URL patterns for the Receipt app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Receipt objects.
"""

from django.urls import path
from Receipt.views import (
    ReceiptListCreateView,
    ReceiptRetrieveUpdateDestroyView,
    GeneratReceiptView,

)

urlpatterns = [
    path('receipts/', ReceiptListCreateView.as_view(), name='receipt-list-create'),
    path('receipts/<int:pk>/', ReceiptRetrieveUpdateDestroyView.as_view(),
         name='receipt-retrieve-update-destroy'),
    path('receipt/<str:receipt_id>/download/', GeneratReceiptView.as_view(), name='generate-receipt')
]
