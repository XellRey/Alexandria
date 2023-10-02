from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Books
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def CartAdd(request, p_id):
    """Добавление Товара в Корзину"""
    cart = Cart(request)
    product_item = Books.objects.get(id=p_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(Books=product_item)
    return redirect('book', p_id)


def CartRemove(request, product_id):
    cart = Cart(request)
    product = Books.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'site/cart.html', {'cart': cart})
