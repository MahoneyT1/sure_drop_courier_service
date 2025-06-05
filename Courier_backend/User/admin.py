"""
    admin file to control what shows up at the backend
"""

from django.contrib import admin
from User.models import User

class BaseAdmin(admin.ModelAdmin):
    """
        Base admin class that provides common functionality for all admin classes.
        It includes search fields, list display, and list filter options.
    """

    search_fields = ['id', 'created_at', 'updated_at']
    list_display = ['id', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


class UserAdmin(BaseAdmin):
    """
        Admin class for the User model.
    """

    list_display = ['id', 'username', 'email', 'full_name', 'is_active', 'is_staff', 'role']
    search_fields = ['username', 'email']
    list_filter = ['is_active', 'is_staff', 'role']
    ordering = ['username']
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'role')
        }),
    )

admin.site.register(User, UserAdmin)

