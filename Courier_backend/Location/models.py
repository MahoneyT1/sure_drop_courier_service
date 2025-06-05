from django.db import models
from Courier_backend.models.base import BaseModel
from Package.models import Package


# Create your models here.
class Location(BaseModel):
    """
        Location model that represents a location object.
        It contains fields for the location details and methods for calculating the delivery cost.
    """
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='locations')
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}"
