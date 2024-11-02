from django.urls import path
from . import views  

urlpatterns = [
    # path('', views.ShortenURLView.as_view(), name='shorten_url'),
    # path('short_code', views.RedirectToOriginalView.as_view(), name='redirect_to_original'), 

    path('<str:short_code>/', views.RedirectToOriginalView.as_view(), name='redirect_to_original'), 
    
    
    # function base example
    path('', views.create_short_url, name='create_short_url'),
]