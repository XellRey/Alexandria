from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = LoginForm
    data = {
        'form': form,
    }
    return render(request, 'registration/login.html', data)


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = CustomUserCreationForm

    data = {
        'form': form,
    }

    return render(request, 'registration/signup.html', data)
