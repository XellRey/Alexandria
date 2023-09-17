from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Books
from accounts.forms import CustomUserChangeForm
# Create your views here.


def index(request):
    book = Books.objects.all()
    data = {
        'book': book
    }
    return render(request, 'site/main.html', data)


def catalog(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(name__icontains=q))
        book = Books.objects.filter(search)
    else:
        book = Books.objects.all()

    data = {
        'book': book
    }
    return render(request, 'site/catalog.html', data)


def catalog_genre_det(request):
    book = Books.objects.filter(genre='Detective')
    data = {
        'book': book
    }
    return render(request, 'site/catalog.html', data)


def catalog_genre_det(request):
    book = Books.objects.filter(genre='Detective')
    data = {
        'book': book
    }
    return render(request, 'site/catalog.html', data)


def book(request, book_id):
    book = Books.objects.get(id=book_id)

    data = {
        'book': book
    }
    return render(request, 'site/book.html', data)


def contacts(request):
    return render(request)


def profile(request):
    return render()


def settings(request):
    if request.method == 'POST':
        user_upd_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_upd_form.is_valid():
            user_upd_form.save()
            return redirect('profile')
    else:
        user_upd_form = CustomUserChangeForm(instance=request.user)

    data = {
        'user_upd_form': user_upd_form,
    }
    return render(request, 'site/settings.html', data)
