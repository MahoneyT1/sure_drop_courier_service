"""
This module contains the LocationSerializer class, which is responsible for serializing
and deserializing Location objects. It uses the Django REST Framework's serializers to
convert Location objects to and from JSON format. The LocationSerializer class also includes
validation for the fields and methods for creating and updating Location objects.
"""

from rest_framework import serializers
from Location.models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Location model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'address')

    def create(self, validated_data):
        """
        Create a new Location object with the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Location object with the validated data.
        """ 
        instance.package_id = validated_data.get('package_id', instance.package_id)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
