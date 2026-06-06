from django import forms
from .models import Ticket
from .models import MaterialRequest


class TicketForm(forms.ModelForm):

    class Meta:

        model = Ticket

        fields = [
            'machine',
            'issue',
            'photo'
        ]


class MaterialRequestForm(forms.ModelForm):

    class Meta:

        model = MaterialRequest

        fields = [
            'part_name',
            'quantity',
            'remarks'
        ]