from django.shortcuts import render, redirect, get_object_or_404
from django.views import View 
from .models import ShortenedURL
from .forms import ShortenURLForm

class ShortenURLView(View):
    form_class = ShortenURLForm
    template_name = 'shorten.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            shortened_url = form.save()
            return render(request, 'shortened.html', {'shortened_url': shortened_url})
        return render(request, self.template_name, {'form': form}) 

class RedirectToOriginalView(View):
    def get(self, request, short_code, *args, **kwargs):
        shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
        return redirect(shortened_url.original_url)