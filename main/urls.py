from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/detective/', views.catalog_genre_det, name='detective'),

    path('profile/settings/', views.settings, name='settings'),

    path('catalog/horror/', views.catalog_genre_hor, name='horror'),
    path('catalog/classic/', views.catalog_genre_cls, name='classic'),
    path('catalog/fantasy/', views.catalog_genre_fnt, name='fantasy'),
]
