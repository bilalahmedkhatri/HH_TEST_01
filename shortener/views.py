import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.views import View
from .models import ShortenedURL
from .forms import ShortenURLForm
import random, string

# task or issue
# issue  1. after successfully shorted url, still calling same function on refresh.

logger = logging.getLogger('shortener_logs')

class ShortenURLView(View):
    form_class = ShortenURLForm
    code_length = 6
    template_name = 'shorten.html'
    success_template = 'success.html'
    failed_template = 'failed.html'
    
    def _get_shortened_url_data(self, request, short_url):
        try:
            url_path = reverse('redirect_to_original', kwargs={'short_code': short_url.short_code})
            return request.build_absolute_uri(url_path)
        except Exception as e:
            logger.error(f"Error while generating shortened url data: {str(e)}")
            return None

    def generate_short_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=self.code_length))
            if not ShortenedURL.objects.filter(short_code=code).exists():
                return code
                
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'Link_URL': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_ori_url = form.cleaned_data['original_url']
            try:
                short_code = self.generate_short_code()
                short_url = ShortenedURL.objects.create(original_url=cleaned_ori_url, short_code=short_code)
                full_url = self._get_shortened_url_data(request, short_url)
                if full_url:
                    return render(request, self.success_template, {'link': full_url})
                else:
                    logger.error("Failed to ggeneate full URL")
                    return render(request, self.failed_template, {'error': 'Failed to generate full URL. Please try again'})
            except Exception as e:
                logger.error(f"Error while creating shortened url: {str(e)}")
                return render(request, self.success_template, {'link': full_url})
        else:
            logger.warning("Form validation failed.")
            return render(request, self.failed_template, {'error': 'Failed to generate full URL. Please try again'})
    

def create_short_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            short_url = form.save()
            url_path = reverse('redirect_to_original', kwargs={'short_code': short_url.short_code})
            full_url = request.build_absolute_uri(url_path)
            return render(request, 'success.html', {'link': full_url})
        else:
            return render(request, 'failed.html')
    else:
        form = ShortenURLForm()
    return render(request, 'shorten.html', {'Link_URL': form})


class RedirectToOriginalView(View):
    def get(self, request, short_code, *args, **kwargs):
        shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
        return redirect(shortened_url.original_url)