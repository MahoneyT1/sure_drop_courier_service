from django.contrib import admin
from User.admin import BaseAdmin
from .models import Location



# Register your models here.
class LocationAdmin(BaseAdmin):
    """
        Admin class for the Location model.
    """

    list_display = ['id', 'package_id', 'address']
    search_fields = ['package_id__tracking_number', 'address']
    ordering = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('package_id', 'address')
        }),
    )

admin.site.register(Location, LocationAdmin)
