from django.urls import path
from app import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, CustomerPasswordChangeForm, CustomerPasswordResetForm, CustomerSetPasswordForm

urlpatterns = [
    path('', views.home),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),
    path('minus_cart/', views.minus_cart, name='minus_cart'),
    path('remove_cart/', views.remove_cart, name='remove_cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile_details/<slug:data>', views.mobile, name='mobile_details'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop_details/<slug:data>', views.laptop, name='laptop_details'),
    path('top_wear/', views.top_wear, name='top_wear'),
    path('top_wear_details/<slug:data>', views.top_wear, name='top_wear_details'),
    path('bottom_wear/', views.bottom_wear, name='bottom_wear'),
    path('bottom_wear_details/<slug:data>', views.bottom_wear, name='bottom_wear_details'),

    # path('login/', views.login, name='login'),
    path('account/login', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    # password change
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=CustomerPasswordChangeForm, success_url='/password_change_done/'), name='password_change'),
    path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'), name='password_change_done'),
    # password reset
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=CustomerPasswordResetForm), name='password_reset'),

    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=CustomerSetPasswordForm), name='password_reset_confirm'),

    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('registration/', views.customer_registration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_done/', views.payment_done, name='payment_done'),
]
