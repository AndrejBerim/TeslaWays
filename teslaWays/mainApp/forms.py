from dataclasses import fields
from django.forms import ModelForm
from .models import Member
from django import forms


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['password']
