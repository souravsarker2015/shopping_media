from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    top_wears = Product.objects.filter(category='TW')
    bottom_wears = Product.objects.filter(category='BW')
    mobiles = Product.objects.filter(category='M')
    laptops = Product.objects.filter(category='L')
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    context = {
        'top_wears': top_wears,
        'bottom_wears': bottom_wears,
        'mobiles': mobiles,
        'laptops': laptops,
        'total_item': total_item,
    }
    return render(request, 'app/home.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    item_already_in_cart = False
    total_item = 0
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        total_item = len(Cart.objects.filter(user=request.user))
    context = {
        'product': product,
        'item_already_in_cart': item_already_in_cart,
        'total_item': total_item,
    }
    return render(request, 'app/productdetail.html', context)


@login_required
def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('show_cart')
    else:
        return redirect('account/login/')


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        total_item = 0
        total_item = len(Cart.objects.filter(user=request.user))

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
                'total': total,
                'total_item': total_item,
            }
            return render(request, 'app/addtocart.html', context)
        else:
            return render(request, 'app/emptycart.html')


@login_required
def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()

        amount = 0.0
        total = 0.0
        shipping = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]

        for p in cart_product:
            temp_amount = (p.quantity * p.product.discount_price)
            amount += temp_amount
        total = amount + shipping

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total': total,
        }
        return JsonResponse(data)


@login_required
def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()

        amount = 0.0
        total = 0.0
        shipping = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]

        for p in cart_product:
            temp_amount = (p.quantity * p.product.discount_price)
            amount += temp_amount
        total = amount + shipping

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total': total,

        }
        return JsonResponse(data)


@login_required
def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        total = 0.0
        shipping = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = (p.quantity * p.product.discount_price)
            amount += temp_amount
        total = amount + shipping

        data = {
            'amount': amount,
            'total': total,

        }
        return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    context = {
        'order_placed': op,
    }
    return render(request, 'app/orders.html', context)


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    if data is None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'xiomi' or data == 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)

    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=10000)

    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles, 'total_item': total_item})


def laptop(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
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

    return render(request, 'app/laptop.html', {'laptops': laptops, 'total_item': total_item})


def top_wear(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    if data is None:
        top_wears = Product.objects.filter(category='TW')

    elif data == 'below':
        top_wears = Product.objects.filter(category='TW').filter(discount_price__lt=1000)
    return render(request, 'app/top_wear.html', {'top_wears': top_wears, 'total_item': total_item})


def bottom_wear(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    if data is None:
        bottom_wears = Product.objects.filter(category="BW")
    if data == 'below':
        bottom_wears = Product.objects.filter(category='BW').filter(discount_price__lt=1000)
    return render(request, 'app/bottom_wear.html', {'bottom_wears': bottom_wears, 'total_item': total_item})


# def login(request):
#     return render(request, 'app/login1.html')


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


@login_required
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


@login_required
def address(request):
    addresses = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'addresses': addresses, 'active': 'btn-primary'})


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
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
            'add': add,
            'total': total,
            'cart_items': cart_items,
        }
        return render(request, 'app/checkout.html', context)
    else:
        return render(request, 'app/emptycart.html')


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)

    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


def search_product(request):
    if request.method == "GET":
        q = request.GET.get('q')
        multiple_q = Q(Q(title__icontains=q) | Q(brand__icontains=q))
        product = Product.objects.filter(multiple_q)
        if len(product) == 0:
            product = Product.objects.all()
        context = {'products': product}
        return render(request, 'app/search_items.html', context)
