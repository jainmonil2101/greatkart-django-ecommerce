from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.filter(is_available=True)
    params = {
        'products': products
    }
    return render(request, 'home.html', params)
