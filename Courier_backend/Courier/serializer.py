"""
This module contains the CourierSerializer class, which is responsible for serializing
and deserializing Courier objects. It uses the Django REST Framework's serializers to
convert Courier objects to and from JSON format. The CourierSerializer class also includes
validation for the fields and methods for creating and updating Courier objects.
"""
from rest_framework import serializers
from Courier.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Courier model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """

    class Meta:
        model = Courier
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        """
        Create a new Courier object with the validated data.
        """
        return Courier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Courier object with the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.vehicle_type = validated_data.get('vehicle_type', instance.vehicle_type)
        instance.license_plate = validated_data.get('license_plate', instance.license_plate)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance
