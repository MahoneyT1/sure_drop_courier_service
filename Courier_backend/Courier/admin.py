from django.contrib import admin
from .models import Courier
from User.admin import BaseAdmin



# Register your models here.
class CourierAdmin(BaseAdmin):
    """
        Admin class for the Courier model.
    """

    list_display = ['id', 'email', 'name', 'phone_number', 'vehicle_type', 'license_plate', 'available']
    search_fields = ['name', 'phone_number']
    list_filter = ['vehicle_type']
    ordering = ['created_at']
    
    fieldsets = (
    (None, {
        'fields': ('email', 'name', 'phone_number', 'vehicle_type', 'license_plate', 'available'),
    }),
)


admin.site.register(Courier, CourierAdmin)
