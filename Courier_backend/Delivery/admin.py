from django.contrib import admin
from User.admin import BaseAdmin
from .models import Delivery



# Register your models here.
class DeliveryAdmin(BaseAdmin):
    """
        Admin class for the Delivery model.
    """

    list_display = ['id', 'courier', 'package', 'pickup_time', 'delivery_time', 'delivery_address', 'delivery_status']
    search_fields = ['courier_id__username', 'package_id__tracking_number']
    list_filter = ['delivery_status']
    ordering = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('courier', 'package', 'delivery_time', 'delivery_address', 'delivery_status')
        }),
    )

admin.site.register(Delivery, DeliveryAdmin)
