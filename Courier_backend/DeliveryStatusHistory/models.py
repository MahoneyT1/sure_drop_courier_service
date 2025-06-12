from django.db import models
from django.utils import timezone


class DeliveryStatusHistory(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("in_transit", "In Transit"),
        ("arrived", "Arrived"),
        ("delivered", "Delivered"),
    ]

    delivery = models.ForeignKey('Delivery.Delivery', on_delete=models.CASCADE, related_name="histories")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.status} at {self.timestamp}"