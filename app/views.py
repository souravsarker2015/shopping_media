from django.shortcuts import render
from .models import *


def home(request):
    top_wears = Product.objects.filter(category='TW')
    bottom_wears = Product.objects.filter(category='BW')
    mobiles = Product.objects.filter(category='M')

    context = {
        'top_wears': top_wears,
        'bottom_wears': bottom_wears,
        'mobiles': mobiles,
    }
    return render(request, 'app/home.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'app/productdetail.html', context)


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request, data=None):
    if data is None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'xiomi' or data == 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    return render(request, 'app/customerregistration.html')


def checkout(request):
    return render(request, 'app/checkout.html')
