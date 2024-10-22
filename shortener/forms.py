from django import forms
from .models import ShortenedURL

class ShortenURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = '__all__'
        
        label = {
            'original_url': 'original_url',
            'short_code': 'Short Code',
        }
        
        widget = {
            'url' : forms.TextInput(attrs={'placeholder': 'URL'}),
            'short_code' : forms.TextInput(attrs={'readonly': True}),
            
        }
        