import random
import string
import logging
import base64
from urllib.parse import urlparse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import ShortenedURLModel
from .forms import ShortenURLForm

logger = logging.getLogger('logs')


class ShortenURLView(View):
    form_class = ShortenURLForm
    template_name = 'shorten.html'
    success_template = 'success.html'
    failed_template = 'failed.html'

    def _get_shortened_url_data(self, request, short_url):
        try:
            url_path = reverse('redirect_to_original', kwargs={
                               'short_code': short_url.short_code})
            return request.build_absolute_uri(url_path)
        except Exception as e:
            logger.error(
                f"Error while generating shortened url data: {str(e)}")
            return None

    def generate_short_code(self):
        while True:
            code = ''.join(random.choices(
                string.ascii_letters + string.digits, k=6))
            if not ShortenedURLModel.objects.filter(short_code=code).exists():
                return code

    def address_encoded(self, url):
        return base64.b64encode(str(url).encode('utf-8'))

    def get_name(self, url):
        url = urlparse(url)
        url_name = url.netloc
        if "." in url_name:
            name = url_name.split('.')
            return name[1]
        else:
            # local host name like localhost
            return url_name

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'Link_URL': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_ori_url = form.cleaned_data['original_url']
            url_bytes = self.address_encoded(cleaned_ori_url)
            try:
                name = self.get_name(cleaned_ori_url)
                short_code = self.generate_short_code()
                short_url = ShortenedURLModel.objects.create(
                    name=name, original_url=cleaned_ori_url, short_code=short_code, url_bytes=url_bytes)
                full_url = self._get_shortened_url_data(request, short_url)
                return render(request, self.success_template, {'link': full_url, 'name': name})
            except Exception as e:
                logger.error(f"Error while creating shortened url: {str(e)}")
                return render(request, self.failed_template, {'error': 'Failed to generate full URL. Please try again'})
        else:
            incorrect_url = form.clean_original_url()
            return render(request, self.failed_template, {'error': incorrect_url})


class RedirectToOriginalView(View):

    def get(self, request, short_code, *args, **kwargs):
        shortened_url = get_object_or_404(
            ShortenedURLModel, short_code=short_code)
        url_bytes = base64.b64decode(shortened_url.url_bytes).decode('utf-8')
        return redirect(url_bytes)
