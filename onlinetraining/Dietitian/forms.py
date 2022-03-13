from django import forms

from .models import DietitianProfile
from .models import PracticeLocation


class DietModel(forms.ModelForm):
    class Meta:
        model = DietitianProfile
        fields = [
            'First_name',
            'Last_name',
            'Phone_number',
            'Country',
            'Email'

        ]


class PracticeLocationModel(forms.ModelForm):
    class Meta:
        model = PracticeLocation
        fields = [
            'Latitude',
            'Longitude',
            'Phone_number',
            'Street',
            'City',
            'Country'


        ]