from django import forms
from django.forms import ModelForm
from .models import Router

class RouterForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Router
        fields = ['hostname',
                  'address',
                  'state',
                  'username',
                  'password',
                  'ticketnumber',
                  'created_at']
