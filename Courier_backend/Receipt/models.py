from django.db import models
from Courier_backend.models.base import BaseModel
from Package.models import Package
from User.models import User


# Create your models here.
class Receipt(BaseModel):
    """
        Receipt model that represents a receipt object.
        It contains fields for the receipt details and methods for calculating the delivery cost.
    """

    PAYMENT_STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('paid', 'Paid')
    )
    package = models.OneToOneField(Package, on_delete=models.CASCADE, related_name='receipt')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    html_content = models.TextField(null=False, blank=False)
    issued_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(default='paid', choices=PAYMENT_STATUS_CHOICE, max_length=20)
    
    def __str__(self):
        return f"{self.package} {self.amount}"