from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('exit/', authViews.LogoutView.as_view(next_page='login'), name='exit'),
]