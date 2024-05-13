from django.shortcuts import render

from goods.models import Products

# Create your views here.

def index(request):

    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'title': 'Home - продукт',
        'product': product,
    }
    return render(request, "goods/product.html", context)