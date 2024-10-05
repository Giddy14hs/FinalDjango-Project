# myapp/urls.py
from django.urls import path
from . import views  # Import your views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # This should map to your home view
     
]
