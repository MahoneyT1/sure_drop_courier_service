"""
This module contains the PackageSerializer class, which is responsible for serializing
and deserializing Package objects. It uses the Django REST Framework's serializers to
convert Package objects to and from JSON format. The PackageSerializer class also includes
validation for the fields and methods for creating and updating Package objects.
"""

from rest_framework import serializers
from Package.models import Package
from Delivery.serializer import DeliverySerializer
from Location.serializer import LocationSerializer
from User.serializer import UserSerializer


class PackageSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Package model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """
    deliveries = serializers.SerializerMethodField(read_only=True)
    location = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Package
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')

    def get_deliveries(self, obj):
        # Implement logic to return deliveries here
        return DeliverySerializer(obj.deliveries.all(), many=True).data

    def get_location(self, obj):
        # Implement logic to return deliveries here
        return LocationSerializer(obj.deliveries.all(), many=True).data

    def create(self, validated_data):
        """
        Create a new Package object with the validated data.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

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
