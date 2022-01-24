from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *


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
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('show_cart')


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)

        amount = 0.0
        total = 0.0
        shipping_amount = 50

        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for p in cart_product:
                temp_amount = p.quantity * p.product.discount_price
                amount += temp_amount
            total = amount + shipping_amount

            context = {
                'carts': cart,
                'amount': amount,
                'total': total
            }
            return render(request, 'app/addtocart.html', context)
        else:
            return render(request, 'app/emptycart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


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


# def login(request):
#     return render(request, 'app/login.html')


def customer_registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration has been done successfully!!!')
            form.save()
    else:
        form = CustomerRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'app/customerregistration.html', context)


def profile(request):
    if request.method == "POST":
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, 'Congratulations Profile has been updated !!')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
    else:
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


def address(request):
    addresses = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'addresses': addresses, 'active': 'btn-primary'})


def checkout(request):
    return render(request, 'app/checkout.html')
