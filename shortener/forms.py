from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.core import validators
from .models import ShortenedURL
from urllib.parse import urlparse

class ShortenURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']
        widget = {
            'original_url' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean_original_url(self):
        original_url = self.cleaned_data.get('original_url')
        parse_url = urlparse(original_url)
        if not parse_url.scheme in ['http', 'https']:
            raise ValidationError("Invalid URL: must start with http:// or https://")
        return escape(original_url)
        