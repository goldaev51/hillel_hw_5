from django import forms
from django.forms import ModelForm

from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='1 leg of triangle', min_value=1)
    leg_2 = forms.IntegerField(label='2 leg of triangle', min_value=1)
