from django.db import models
from core.models.base import BaseModel
from User.models import User
import datetime


# Create your models here.
class Package(BaseModel):
    """
        Package model that represents a package object.
        It contains fields for the package details and methods for calculating the delivery cost.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages')
    recipient_name = models.CharField(max_length=255, null=False, blank=False)
    recipient_phone_number = models.CharField(max_length=20, null=False, blank=False)
    recipient_address = models.CharField(max_length=255, null=False, blank=False)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    description = models.TextField(null=True, blank=True, max_length=225)
    pickup_date = models.DateField(null=False, blank=False, max_length=50, default=datetime.datetime.now)

    def __str__(self):
        """return string representation of user model"""
        return f'{self.recipient_name}, {self.recipient_phone_number}, {self.recipient_address}'
    
    def create_delivery(self, delivery_type, delivery_address, delivery_date):
        """method to create a delivery for the package"""
        from Delivery.models import Delivery
        from Courier.models import Courier
        from random import choice

        # Select a random courier for simplicity; in real scenarios, this would be more complex
        courier = Courier.objects.filter(available=True).first()
        
        if not courier:
            raise ValueError("No available courier found")

        delivery = Delivery.objects.create(
            courier=courier,
            package=self,
            delivery_type=delivery_type,
            delivery_address=delivery_address,
            estimated_delivery_date=delivery_date
        )
        return delivery
    