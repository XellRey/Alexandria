from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/detective/', views.catalog_genre_det, name='detective')
]
