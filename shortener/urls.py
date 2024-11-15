from django.urls import path
from . import views  

urlpatterns = [
    path('', views.ShortenURLView.as_view(), name='create_short_url_class'),
    path('<str:short_code>/', views.RedirectToOriginalView.as_view(), name='redirect_to_original'),
]