from django.contrib import admin
from .models import Package


# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    """
        Admin class for the Package model.
    """

    list_display = [field.name for field in Package._meta.fields]
    search_fields = ['recipient_name']
    list_filter = ['recipient_name']
    ordering = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('recipient_name', 'weight', 'height', 'length', )
        }),
    )

admin.site.register(Package, PackageAdmin)
