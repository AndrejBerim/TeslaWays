from django import forms
from . models import Place


class PlaceForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Place
        fields = ['address', ]
