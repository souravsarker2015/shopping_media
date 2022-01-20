from django.shortcuts import render
from .models import *


def home(request):
    top_wears = Product.objects.filter(category='TW')
    bottom_wears = Product.objects.filter(category='BW')
    mobiles = Product.objects.filter(category='M')
    laptops = Product.objects.filter(category='L')
    context = {
        'top_wears': top_wears,
        'bottom_wears': bottom_wears,
        'mobiles': mobiles,
        'laptops': laptops,
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

    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=10000)

    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def laptop(request, data=None):
    if data is None:
        laptops = Product.objects.filter(category="L")
    elif data == 'asus' or data == 'hp' or data == 'dell':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below30':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=30000)
    elif data == 'below40':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=40000)
    elif data == 'below50':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=50000)
    elif data == 'below60':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=60000)

    return render(request, 'app/laptop.html', {'laptops': laptops})


def top_wear(request, data=None):
    if data is None:
        top_wears = Product.objects.filter(category='TW')

    elif data == 'below':
        top_wears = Product.objects.filter(category='TW').filter(discount_price__lt=1000)
    return render(request, 'app/top_wear.html', {'top_wears': top_wears})


def bottom_wear(request, data=None):
    if data is None:
        bottom_wears = Product.objects.filter(category="BW")
    if data == 'below':
        bottom_wears = Product.objects.filter(category='BW').filter(discount_price__lt=1000)
    return render(request, 'app/bottom_wear.html', {'bottom_wears': bottom_wears})


def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    return render(request, 'app/customerregistration.html')


def checkout(request):
    return render(request, 'app/checkout.html')
