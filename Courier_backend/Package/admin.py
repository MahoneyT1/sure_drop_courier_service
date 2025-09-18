from django.contrib import admin
from .models import Package
from Courier.models import Courier
from Delivery.models import Delivery
from .forms import PackageForm


# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    """
        Admin class for the Package model.
    """
    form = PackageForm

    list_display = ['recipient_name', 'recipient_phone_number', 
                    'recipient_address', 'description', 'pickup_date',
                    'weight', 'height', 'length', 'width', 'created_at']

    search_fields = ['recipient_name']
    list_filter = ['recipient_name']
    ordering = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('recipient_name', 'recipient_phone_number', 
                       'recipient_address', 'description', 'pickup_date',
                       'weight', 'height', 'length', 'width', 'delivery_type', 
                       'delivery_address')
        }),
    )

    def save_model(self, request, obj, form, change):
        """Override save_model to set the user field automatically."""
        obj.user = request.user

        delivery_type = form.cleaned_data.get('delivery_type', 'domestic')
        
        delivery_address = form.cleaned_data.get('delivery_address', '')
        delivery_date = form.cleaned_data.get('pickup_date', None)

        if not obj.deliveries and hasattr(obj, 'create_delivery'):
            delivery = obj.create_delivery(
                delivery_type=delivery_type,
                delivery_address=delivery_address,
                delivery_data=delivery_date
            )

        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in '{field}': {error}")
        super().save_model(request, obj, form, change)

admin.site.register(Package, PackageAdmin)
