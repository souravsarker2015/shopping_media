from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile_details/<slug:data>', views.mobile, name='mobile_details'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop_details/<slug:data>', views.laptop, name='laptop_details'),
    path('top_wear/', views.top_wear, name='top_wear'),
    path('top_wear_details/<slug:data>', views.top_wear, name='top_wear_details'),
    path('bottom_wear/', views.bottom_wear, name='bottom_wear'),
    path('bottom_wear_details/<slug:data>', views.bottom_wear, name='bottom_wear_details'),

    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]
