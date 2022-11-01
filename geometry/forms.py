from django import forms


class HypoForm(forms.Form):
    catet = forms.IntegerField(label='Enter catet 1', min_value=1)
    catet2 = forms.IntegerField(label='Enter catet 2', min_value=1)
