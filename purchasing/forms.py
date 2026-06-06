from django import forms

from .models import PurchaseRequest


class PurchaseRequestForm(forms.ModelForm):

    class Meta:

        model = PurchaseRequest

        fields = [
    'part_name',
    'quantity',
    'notes'
]
        
class PurchasingUpdateForm(forms.ModelForm):

    class Meta:

        model = PurchaseRequest

        fields = [
            'supplier',
            'estimated_cost',
            'eta'
        ]