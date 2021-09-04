from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from product.models.book import Book

from .cart import Cart
from .models import Order, OrderItem


#
# def cart_add(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         book_id = int(request.POST.get('bookid'))
#         book_qty = int(request.POST.get('bookqty'))
#         book = get_object_or_404(Book, id=book_id)
#         cart.add(book=book, book_qty=book_qty)
#
#         cart_qty = cart.__len__()
#         response = JsonResponse({'qty': cart_qty})
#         return response

def cart_add(request):
    if request.method == "POST":
        item = Book.objects.get(id=request.POST['book_id'])
        try:
            customer = request.user
            order, created = Order.objects.get_or_create(owner=customer, status='سبد خرید')
            order_item, created = OrderItem.objects.get_or_create(order=order, book=item)
            order_item.quantity = request.POST['quantity']
            order_item.save()
        except:
            pass
    return redirect('book_list')


class CartItems(ListView):
    model = Order
    template_name = 'cart_items.html'


class OrderItemList(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['details'] = context['order'].items.all()
        return context
