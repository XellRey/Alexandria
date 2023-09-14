from django.db.models import Q
from django.shortcuts import render
from .models import Books
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


def contacts(request):
    return render(request)


def about_us(request):
    return render(request)


def profile(request):
    return render()