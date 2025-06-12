"""
This module contains the DeliverySerializer class, which is responsible for serializing
and deserializing Delivery objects. It uses the Django REST Framework's serializers to
convert Delivery objects to and from JSON format. The DeliverySerializer class also includes
validation for the fields and methods for creating and updating Delivery objects.
"""
from rest_framework import serializers
from Delivery.models import Delivery
from Courier.serializer import CourierSerializer
from DeliveryStatusHistory.serializer import DeliveryStatusHistorySerializer


class DeliverySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Delivery model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """
    courier = CourierSerializer(read_only=True)
    histories = DeliveryStatusHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'histories')

    def create(self, validated_data):
        """
        Create a new Delivery object with the validated data.
        """
        return Delivery.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Delivery object with the validated data.
        """
        instance.courier = validated_data.get('courier', instance.courier)
        instance.package = validated_data.get('package', instance.package)
        instance.status = validated_data.get('status', instance.status)
        instance.delivery_time = validated_data.get('delivery_time', instance.delivery_time)
        instance.save()
        return instance
