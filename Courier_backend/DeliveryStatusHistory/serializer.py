"""
    Delivery serializer
"""
from rest_framework import serializers
from DeliveryStatusHistory.models import DeliveryStatusHistory


class DeliveryStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatusHistory
        fields = ['status', 'timestamp']
