from django.http import JsonResponse
from .models import Product
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
def product_list(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)
class HomeView(TemplateView):
    template_name = 'myapp/home.html'

def home(request):
    return render(request, 'myapp/home.html')



