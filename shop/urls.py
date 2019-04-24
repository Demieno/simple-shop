"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop_main.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = 'main'),
    path('index/',index, name = 'main'),
    path('product/<product_slug>/',product, name = 'product'),
    path('category/<category_slug>/',category, name = 'category'),
    
    ##
    path('cart/',cart, name = 'cart'),
    path('add/<product_slug>/',add_to_cart, name = 'add'),
    path('increase/<product_slug>/',increase_item, name = 'increase'),
    path('remove/<product_slug>/',remove_from_cart, name = 'remove'),
    path('decrease/<product_slug>/',decrease_item, name = 'decrease'),
    
    ##
    path('login/',login, name = 'login'),
    path('logout/',logout, name = 'logout'),
    path('registration/',registration, name = 'registration'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)