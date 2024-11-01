from django import forms
from django.core import validators
from .models import ShortenedURL

class ShortenURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']
        
        label = {
            'for': 'original_url',
        }
        
        widget = {
            'original_url' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        