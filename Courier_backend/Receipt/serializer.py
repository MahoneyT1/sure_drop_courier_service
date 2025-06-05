"""
This module contains the ReceptSerializer class, which is responsible for serializing
and deserializing Receipt objects. It uses the Django REST Framework's serializers to
convert Receipt objects to and from JSON format. The ReceiptSerializer class also includes
validation for the fields and methods for creating and updating Receipt objects.
"""

from rest_framework import serializers
from Receipt.models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Receipt model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """

    class Meta:
        model = Receipt
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'htm_content')

    def create(self, validated_data):
        """
        Create a new Receipt object with the validated data.
        """
        return Receipt.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Receipt object with the validated data.
        """     
        instance.package_id = validated_data.get('package_id', instance.package_id)
        instance.delivery_id = validated_data.get('delivery_id', instance.delivery_id)