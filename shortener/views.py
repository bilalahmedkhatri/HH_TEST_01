from django.shortcuts import render, redirect, get_object_or_404
from django.views import View 
from .models import ShortenedURL
from .forms import ShortenURLForm

# class ShortenURLView(View):
#     form_class = ShortenURLForm
#     template_name = 'shorten.html'

#     """TEST DATA ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'auser', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']"""

#     def get(self, request, *args, **kwargs):
#         print('TEST DATA', dir(request))
#         return render(request, self.template_name, )

#     def post(self, request, *args, **kwargs):
#         print("result : ", request.POST)
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             shortened_url = form.save()
#             return render(request, self.template_name, {'shortened_url': shortened_url})
#         return render(request, self.template_name, {'form': form})


def create_short_url(request):
    if request.method == 'POST':
        get_data_form = ShortenURLForm(request.POST)
        if get_data_form.is_valid():
            short_url = get_data_form.save()
            main_domain = request.META.get('HTTP_REFERER')
            link = f"{main_domain}{short_url}"
            return render(request, 'success.html', {'link': link})

        else:
            return render(request, 'failed.html')
    else:
        get_data_form = ShortenURLForm()
    return render(request, 'shorten.html', {'Link_URL': get_data_form})


class RedirectToOriginalView(View):
    def get(self, request, short_code, *args, **kwargs):
        shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
        return redirect(shortened_url.original_url)