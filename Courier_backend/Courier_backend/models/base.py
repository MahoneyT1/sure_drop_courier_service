"""
    The base class that other models will inherit from.
    It contains common fields and methods that are shared across all models.
    This class is not meant to be used directly, but rather as a base for other models.
"""

from django.db import models
import uuid


class BaseModel(models.Model):
    """
        Base model class that provides common fields 
        and methods for all models.
    """

    id = models.UUIDField(primary_key=True, editable=False, unique=True, auto_created=True, default=uuid.uuid4 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

