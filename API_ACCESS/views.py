from django.shortcuts import render
from django.views import View

# Create your views here.


class LinkView(View):
    
    template_name = None
    
    def get(self, request, *args, **kwargs):
        # context = self.get_context_data()
        # original_url = request.POST['original_url']
        return render(request, self.template_name)
    
    def post(self, request):
        original_url = request.POST['original_url']
        short_url = short_url_generator(original_url)


def shorten_link(request):
    if request.method == 'Post':
        original_url = request.POST['original_url']
    return render(request, 'link_template/base.html')



