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
    