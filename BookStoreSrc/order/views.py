from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Order
from .cart import Cart
from product.models.book import Book


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        book = get_object_or_404(Book, id=book_id)
        cart.add(book=book, book_qty=book_qty)

        cart_qty = cart.__len__()
        response = JsonResponse({'qty': cart_qty})
        return response


class CartItems(ListView):
    model = Order
    template_name = 'cart_items.html'
