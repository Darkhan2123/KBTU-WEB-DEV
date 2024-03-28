from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Category
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)

def product_detail(request, id):
    product = get_object_or_404(Product, id = id)
    data = {'product': model_to_dict(product)}
    return JsonResponse(data)

def category_list(request):
    categories = Category.objects.all()
    data = {'categories': list(categories.values())}
    return JsonResponse(data)

def category_detail(request, id):
    category = get_object_or_404(Category, id = id)
    data = {'category': model_to_dict(category)}
    return JsonResponse(data)

def category_products(request, id):
    category = get_object_or_404(Category, id = id)
    products = Product.objects.filter(category = category)
    data = {'products': list(products.values())}
    return JsonResponse(data)



