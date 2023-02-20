from django.shortcuts import render
from .models import Product

# Create your views here.

def product(request):
    return render(request, 'products/product.html')

def product(request):
    pro = Product.objects.all()
    x = {'pro':pro.filter(price__range=(10,500))}
    return render(request, 'products/products.html', x)
