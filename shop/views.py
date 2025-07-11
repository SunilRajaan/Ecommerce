from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    allProds = []
    catprods = Product.objects.values('category')  
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        products_by_slide = [prod[i:i + 4] for i in range(0, n, 4)]
        allProds.append([products_by_slide, cat, range(nSlides)])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('We are at Contact')

def tracker(request):
    return HttpResponse('We are at Tracker')

def search(request):
    return HttpResponse('We are at Search')

def productview(request):
    return HttpResponse('We are at Product View')

def checkout(request):
    return HttpResponse('We are at Checkout')
