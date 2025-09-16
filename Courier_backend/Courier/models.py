from django.db import models

# Create your models here.
from core.models.base import BaseModel


class Courier(BaseModel):
    """
        Courier model that represents a courier object.
        It contains fields for the courier details and methods for calculating the delivery cost.
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    vehicle_type = models.CharField(max_length=50, null=False, blank=False)
    license_plate = models.CharField(max_length=20, unique=True, null=False, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type} - {self.license_plate}"
