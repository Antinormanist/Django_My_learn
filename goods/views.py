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

def about(request):
    context = {
        "title": "О нас"
    }
    # return render(request, "goods/about.html", context)