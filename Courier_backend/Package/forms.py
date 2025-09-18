"""form for the Package model in the admin interface."""

from django import forms
from .models import Package


class PackageForm(forms.ModelForm):
    """Form for the Package model in the admin interface."""

    delivery_type = forms.CharField(required=True)
    delivery_address = forms.CharField(required=True)
    

    class Meta:
        model = Package
        fields = ['recipient_name', 'recipient_phone_number', 
                  'recipient_address', 'description', 'pickup_date', 
                  'weight', 'height', 'length', 'width',
                ]
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'delivery_type': forms.Select(choices=[
                ('domestic', 'Domestic'),
                ('international', 'International')
            ]),
            'delivery_address': forms.TextInput(attrs={'size': 50}),
            'recipient_address': forms.TextInput(attrs={'size': 50}),
            'recipient_name': forms.TextInput(attrs={'size': 50}),
            'recipient_phone_number': forms.TextInput(attrs={'size': 20}),
            'weight': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
            'height': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
            'length': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
            'width': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        delivery_type = cleaned_data.get('delivery_type')
        delivery_address = cleaned_data.get('delivery_address')

        if not delivery_type:
            self.add_error('delivery_type', 'This field is required.')

        if not delivery_address:
            self.add_error('delivery_address', 'This field is required.')

        return cleaned_data
    
