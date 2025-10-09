"""
    User object to modify django custom User entity
"""
from django.contrib.auth.models import ( 
    AbstractBaseUser, BaseUserManager, PermissionsMixin )

from rest_framework.response import Response
from rest_framework import status
from django.db import models
from uuid import uuid4
from core.models.base import BaseModel

# user custom manger(manages the creation of user objects)
class CustomUserManager(BaseUserManager):
    """
        manages user creation and based of User-Type
        user ==> Admin or Default
    """

    def create_user(self, email, username, password=None, **extra_fields):
        """method creates user by validating the user data
        to make sure that all requirements are met
        """

        if not email:
            # return an error response
            raise ValueError("email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    # create admin user
    def create_superuser(self, email, username, password=None, **extra_fields):
        """method that creates super user
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email=email, username=username, password=password, **extra_fields)
    

 # function that generates uuid

def generate_uuid():
    """generates uuid"""
    return uuid4()   

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """Actual user Table
    """

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('courier', 'Courier'),
        ('user', 'User'),
    )

    email = models.EmailField(unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=150,null=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, default="default_user")
    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=150, null=True)
    role = models.CharField(max_length=20, default='user', choices=ROLE_CHOICES)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id} {self.username}'

