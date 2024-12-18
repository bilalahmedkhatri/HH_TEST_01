import logging
from django import forms
from django.utils.html import escape
from .models import ShortenedURLModel
from urllib.parse import urlparse

logger = logging.getLogger('logs')


class ShortenURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURLModel
        fields = ['original_url']
        widget = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_original_url(self):
        original_url = self.cleaned_data.get('original_url')
        parse_url = urlparse(original_url)
        if not parse_url.scheme in ['http', 'https']:
            logger.warning('request not from http or https')
            return "Request not from http or https"
        return escape(original_url)
