from django import forms
from .models import Car        # importa tu modelo

class CarForm(forms.ModelForm):
    class Meta:
        model  = Car
        fields = [
            'make', 'model', 'year',
            'mileage_km', 'fuel_type',
            'price_clp', 'image',
        ]