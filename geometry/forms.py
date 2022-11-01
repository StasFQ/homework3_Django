from django import forms


class HypoForm(forms.Form):
    catet = forms.IntegerField(label='Enter first catet', min_value=1)
    catet2 = forms.IntegerField(label='Enter second catet', min_value=1)
