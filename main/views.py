from django.shortcuts import render
from .models import Books
# Create your views here.


def index(request):
    book = Books.objects.all()
    data = {
        'book': book
    }
    return render(request, 'site/main.html', data)
