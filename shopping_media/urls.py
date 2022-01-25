from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from app.forms import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('app.urls')),
                  path('account/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
                  path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
