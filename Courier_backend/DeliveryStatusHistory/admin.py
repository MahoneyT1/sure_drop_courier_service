from django.contrib import admin
from .models import DeliveryStatusHistory

# Register your models here.
class DeliveryStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ['delivery', 'status', 'timestamp']
    search_fields = ['status']
    list_filter = ['status']
    ordering = ['timestamp']
    fieldsets = (
        (None, {
            'fields': ('delivery', 'status', 'timestamp')
        }),
    )

admin.site.register(DeliveryStatusHistory, DeliveryStatusHistoryAdmin)

