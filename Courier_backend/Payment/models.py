from django.db import models
from Courier_backend.models.base import BaseModel
from User.models import User
from Package.models import Package


# Create your models here.
class Payment(BaseModel):
    """
        Payment model that represents a payment object.
        It contains fields for the payment details and methods for calculating the delivery cost.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    payment_method = models.CharField(max_length=50, null=False, blank=False)
    payment_status = models.CharField(max_length=50, null=False, blank=False)
    transaction_id = models.CharField(max_length=255, unique=True, null=False, blank=False)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='payments')