from django.urls import path
from . import views  

urlpatterns = [
    path('shorten/', views.ShortenURLView.as_view(), name='shorten_url'),
    path('short_code', views.RedirectToOriginalView.as_view(), name='redirect_to_original'), 

    # path('<str:short_code>/', views.RedirectToOriginalView.as_view(), name='redirect_to_original'), 
]