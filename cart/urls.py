from django.urls import path
from django.urls import include, re_path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<p_id>\d+)/$', views.CartAdd, name='CartAdd'),
 ]