from django import forms
from .models import FoodOrder

class FoodOrderForm(forms.ModelForm):
    class Meta:
        model = FoodOrder
        fields = '__all__'
