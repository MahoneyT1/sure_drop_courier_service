from django.db import models
from Package.models import Package
from Courier.models import Courier
from Courier_backend.models.base import BaseModel


DELIVERY_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('in_transit', 'In Transit'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
)

DELIVERY_TYPE_CHOICE = (
    ('domestic', 'Domestic'),
    ('international', 'International')
)


class Delivery(BaseModel):
    """ 
        Delivery model that represents a delivery object.
        It contains fields for the delivery details and methods for calculating the delivery cost.
    """
    courier = models.ForeignKey('Courier.Courier', on_delete=models.CASCADE, related_name='deliveries')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='deliveries')
    pickup_time = models.DateTimeField(max_length=50, null=True, blank=True)
    delivery_time = models.DateTimeField(max_length=40 ,null=False, blank=False)
    delivery_address = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=50, choices=DELIVERY_TYPE_CHOICE, default='domestic')
    delivery_status = models.CharField(max_length=50, choices=DELIVERY_STATUS_CHOICES, default='pending')

    def __str__(self):
        """return string representation of user model"""
        return f'{self.package}, {self.courier}, {self.pickup_time}'
