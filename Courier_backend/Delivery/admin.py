from django.contrib import admin
from User.admin import BaseAdmin
from .models import Delivery



# Register your models here.
class DeliveryAdmin(BaseAdmin):
    """
        Admin class for the Delivery model.
    """

    list_display = ['id', 'courier', 'package', 'current_status', 'estimated_delivery_date', 'delivery_address']
    search_fields = ['courier_id__username', 'package_id__tracking_number']
    list_filter = ['current_status']
    ordering = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('courier', 'package', 'current_status', 'delivery_address', 'estimated_delivery_date')
        }),
    )

    def save_model(self, request, obj, form, change):
        old_status = None

        if obj.pk:
            old_status = Delivery.objects.get(pk=obj.pk).current_status

        super().save_model(request, obj, form, change)

        if old_status and old_status != obj.current_status:
            obj.update_status(obj.current_status)


admin.site.register(Delivery, DeliveryAdmin)
