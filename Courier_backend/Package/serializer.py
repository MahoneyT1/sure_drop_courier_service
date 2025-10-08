"""
This module contains the PackageSerializer class, which is responsible for serializing
and deserializing Package objects. It uses the Django REST Framework's serializers to
convert Package objects to and from JSON format. The PackageSerializer class also includes
validation for the fields and methods for creating and updating Package objects.
"""

from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import traceback
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string


from Package.models import Package
from Delivery.serializer import DeliverySerializer
from DeliveryStatusHistory.serializer import DeliveryStatusHistorySerializer
from User.serializer import UserSerializer
from Receipt.serializer import ReceiptSerializer
from Courier.models import Courier
from Delivery.models import Delivery
from DeliveryStatusHistory.models import DeliveryStatusHistory
from Receipt.models import Receipt





class PackageSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Package model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """
    deliveries = DeliverySerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    delivery_history = DeliveryStatusHistorySerializer(source='delivery.histories', many=True, read_only=True)
    receipt = ReceiptSerializer(read_only=True)


    class Meta:
        model = Package
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'user', 
                            'delivery_history', 'receipt')

    def get_deliveries(self, obj):
        # Implement logic to return deliveries here
        return DeliverySerializer(obj.deliveries.all(), many=True).data
    
    def create(self, validated_data):
        """
        Create a new Package object with the validated data.
        """
        request = self.context.get('request')

        user = request.user if request else None

        delivery_type = request.data.pop('delivery_type') if request and\
        'delivery_type' in request.data else 'domestic'

        package = Package.objects.create(
            user=user,
            **validated_data
        )
 
        # now search for available courier to handle each shipment
        assign_courier = Courier.objects.filter(available=True).first()

        if not assign_courier:
            raise serializers.ValidationError("No available courier found")

        # create a delivery and assign courier and package in it                
        # create a delivery and to track both courier and the package
        delivery = Delivery.objects.create(
            courier=assign_courier,
            package=package,
            delivery_type=delivery_type,
            estimated_delivery_date=validated_data.get('pickup_date'),
            delivery_address=serializerPackage.validated_data.get('recipient_address'),
        )
        
        # create a location
        
        delivery_history =  DeliveryStatusHistory.objects.create(
            delivery=delivery,
            status='created',
        )
        delivery_history = delivery_history.save()
        serialized_delivery_history =  DeliveryStatusHistorySerializer(delivery_history)
            
        # create Receipt

        receipt = Receipt.objects.create(
            package=package,
            amount=2000,
            )

        # render a html template in the attribute of the created Receipt
        html_string = render_to_string('receipt.html', {'receipt': receipt})
        receipt.html_content = html_string
        receipt.save()
        
        return package

    def update(self, instance, validated_data):
        """
        Update an existing Package object with the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.length = validated_data.get('length', instance.length)
        instance.save()
        return instance

