from django.shortcuts import render
from django.views import View

# Create your views here.

class LinkView(View):
    
    def get(self, request):
        original_url = request.POST['original_url']
        return render(request, 'link_template/shorter.html')
    
    def post(self, request):
        original_url = request.POST['original_url']
        short_url = short_url_generator(original_url)


def shorten_link(request):
    if request.method == 'Post':
        original_url = request.POST['original_url']
    return render(request, 'link_template/shorter.html')



