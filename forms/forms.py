from django import forms


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='1 leg of triangle', min_value=1)
    leg_2 = forms.IntegerField(label='2 leg of triangle', min_value=1)
