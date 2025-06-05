from django.contrib import admin
from .models import Receipt
from User.admin import BaseAdmin


# Register your models here.
class ReceiptAdmin(BaseAdmin):
    """
        Admin class for the Receipt model.
    """
    

    list_display = ['id', 'package_id', 'amount', 'payment_status']
    search_fields = ['user_id__username', 'package_id__tracking_number']
    list_filter = ['payment_status']
    ordering = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('user_id', 'package_id', 'amount', 'payment_status')
        }),
    )

admin.site.register(Receipt, ReceiptAdmin)
