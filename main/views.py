from django.db.models import Q
from django.shortcuts import render, redirect

from orders.models import Order
from .models import Books
from accounts.forms import CustomUserChangeForm
from .forms import ContactMessage
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

def catalog_genre_hor(request):
    book = Books.objects.filter(genre='Horror')
    data = {
        'book': book
    }
    return render(request, 'site/catalog.html', data)


def catalog_genre_cls(request):
    book = Books.objects.filter(genre='Classic')
    data = {
        'book': book
    }
    return render(request, 'site/catalog.html', data)

def catalog_genre_fnt(request):
    book = Books.objects.filter(genre='Fantasy')
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
    forms = ContactMessage()
    if request.method == 'POST':
        forms = ContactMessage(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('contacts')
    data = {
        'forms': forms
    }
    return render(request, 'site/contacts.html', data)


def profile(request):
    orders = Order.objects.filter(user=request.user)

    data = {
        'orders':orders
    }
    return render(request, 'site/profile.html', data)


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


def book(request, book_id):
    book = Books.objects.get(id=book_id)
    data = {
        'book': book
    }
    return render(request, 'site/book.html', data)


def add_to_cart(request, operation, book_id):
    user = request.user
    if operation == 'add':
        order = Order(book=book_id, user=user)
        order.save()
    back = request.META.get('HTTP_REFERER')

    return redirect(back, book_id)




