from django.db import models
from Package.models import Package
from Courier.models import Courier
from core.models.base import BaseModel
from DeliveryStatusHistory.models import DeliveryStatusHistory


DELIVERY_STATUS_CHOICES = (
    ('created', 'Created'),
    ('on_transit', 'On Transit'),
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
    estimated_delivery_date = models.DateField(null=True, blank=True)
    delivery_address = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=50, choices=DELIVERY_TYPE_CHOICE, default='domestic')
    current_status = models.CharField(max_length=50, choices=DELIVERY_STATUS_CHOICES, default='created')

    def __str__(self):
        """return string representation of user model"""
        return f'{self.package}, {self.courier}, {self.current_status}'

    def update_status(self, new_status):
        self.current_status = new_status
        self.save()
        DeliveryStatusHistory.objects.create(delivery=self, status=new_status)