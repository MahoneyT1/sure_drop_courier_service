"""
    Receipt views
    This module contains the views for the Receipt app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Receipt objects.
    It uses Django REST Framework's concrete generic to handle the requests
    and responses.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Receipt.models import Receipt
from Receipt.serializer import ReceiptSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Receipt
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML


class ReceiptListCreateView(ListCreateAPIView):
    """
    Api view for listing and creating Receipt objects.
    It uses the ReceiptSerializer class to serialize and deserialize
    Receipt objects.
    """

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list all Receipt objects.
        """
        receipts = self.get_queryset()
        serializer = self.get_serializer(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new Receipt object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ReceiptRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Api view for retrieving, updating, and deleting Receipt objects.
    It uses the ReceiptSerializer class to serialize and deserialize
    Receipt objects.
    """

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a specific Receipt object.
        """
        receipt = self.get_object()
        serializer = self.get_serializer(receipt)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a specific Receipt object.
        """
        receipt = self.get_object()
        serializer = self.get_serializer(receipt, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a specific Receipt object.
        """
        receipt = self.get_object()
        receipt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view for generating receipt
class GeneratReceiptView(APIView):
    """Generate the receipt view and template/ string
    """

    def get(self, request, receipt_id):
        receipt = get_object_or_404(Receipt, id=receipt_id)
        package = receipt.package

        # parse the html file to be converted to a binary
        html_string = render_to_string(
            'receipt.html', 
            {
                'receipt': receipt,
                'package': package,
            })

        pdf_file = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['content-Disposition'] = f'attachment; filename=receipt_{receipt_id}.pdf'
        return response
