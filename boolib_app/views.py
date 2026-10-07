from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'boolib_app/products.html', {'products': products})