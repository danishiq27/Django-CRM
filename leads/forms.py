from django import forms
from .models import Leads
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User=get_user_model()

class Leadform(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    age=forms.IntegerField(min_value=0)


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ('first_name', 'last_name', 'age', 'agent')

class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username",)
        field_classes = {'username': UsernameField}       