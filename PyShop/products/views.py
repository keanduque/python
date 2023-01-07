from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer


# /products -> index url
def index(request):
    products = Product.objects.all()

    return render(request, 'index.html',
                  {'products': products})


def details(request):
    return HttpResponse("Product Details")


def new(request):
    return HttpResponse('New Products')