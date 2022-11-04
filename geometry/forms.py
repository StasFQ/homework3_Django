from django import forms

from .models import Person


class HypoForm(forms.Form):
    catet = forms.IntegerField(label='Enter first catet', min_value=1)
    catet2 = forms.IntegerField(label='Enter second catet', min_value=1)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
