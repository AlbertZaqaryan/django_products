from django.shortcuts import render
from .models import Category, Product
# Create your views here.

def index(request):
    category_list = Category.objects.all()
    return render(request, 'main/index.html', context={
        'category_list':category_list
    })

def products(request, id):
    product_list = Category.objects.filter(pk=id)
    return render(request, 'main/products.html', context={
        'product_list':product_list
    })


def products_detail(request, id):
    one_prod = Product.objects.get(pk=id)
    return render(request, 'main/products_detail.html', context={
        'one_prod':one_prod
    })
