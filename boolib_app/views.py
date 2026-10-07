from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'boolib_app/products.html', {'products': products})


def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genre = request.POST.get('genre')
        min_players = request.POST.get('min_players')
        max_players = request.POST.get('max_players')
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            genre=genre,
            min_players=min_players,
            max_players=max_players,
            price=price,
        )
        messages.success(request, 'Товар успішно додано')
        return redirect('product_list')

    return render(request, 'boolib_app/product_add.html')