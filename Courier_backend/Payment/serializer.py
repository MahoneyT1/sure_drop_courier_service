"""
This module contains the PaymentSerializer class, which is responsible for serializing
and deserializing Payment objects. It uses the Django REST Framework's serializers to
convert Payment objects to and from JSON format. The PaymentSerializer class also includes
validation for the fields and methods for creating and updating Payment objects.
"""

from rest_framework import serializers
from Payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Payment model.
    It defines the fields to be serialized and deserialized,
    as well as validation and creation methods.
    """

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        """
        Create a new Payment object with the validated data.
        """
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Payment object with the validated data.
        """
        instance.amount = validated_data.get('amount', instance.amount)
        instance.method = validated_data.get('method', instance.method)
        instance.status = validated_data.get('status', instance.status)
        instance.transaction_id = validated_data.get('transaction_id', instance.transaction_id)
        instance.save()
        return instance
