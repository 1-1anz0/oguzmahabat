from django.shortcuts import render
from products.models import *
from django.shortcuts import get_list_or_404
from products.utils import search

# Create your views here.

def category(request, category_slug=None):
    categories = Category.objects.all()

    cat_search = request.GET.get('category', None)
    query = request.GET.get('q', None)


    if  category_slug == 'ahli-onumler':
        products = Products.objects.all()

    elif query or cat_search:
        products = search(query, cat_search)
    
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    # categories = Category.objects.get(slug=category_slug)
    

    context = {
        'cat' : categories,
        'products': products,

    }


    return render(request, 'products/category.html', context)

def product_show(request, product_slug):

    product = Products.objects.get(slug__iexact=product_slug)

    context = {
        'product': product
    }

    return render(request, 'products/product.html', context)