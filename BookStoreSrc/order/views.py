from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from product.models.book import Book
from discount.models import BonusDiscount

from .models import Order, OrderItem


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


def in_cart_add(request):
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
    return redirect('cart_items')


class CartItems(ListView):
    model = Order
    template_name = 'cart_items.html'

    def get_context_data(self, **kwargs):
        context = super(CartItems, self).get_context_data()
        user = self.request.user
        try:
            user_cart = self.model.objects.get(owner=user, status='سبد خرید')
        except:
            user_cart = None
        context['cart'] = user_cart
        return context


class OrderItemList(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['details'] = context['order'].items.all()
        return context


def order_item_delete(request, pk):
    try:
        order_item = OrderItem.objects.get(id=pk)
        order_item.delete()
    except:
        pass
    return redirect('cart_items')


def submit_order(request):
    try:
        user = request.user
        my_cart = Order.objects.get(owner=user, status='سبد خرید')
        my_order = Order.objects.get_or_create(owner=user, status='سفارش')[0]
        for item in my_cart.items.all():
            item.book.number_in_stock = item.book.number_in_stock - item.quantity
            item.book.save()
            item.order = my_order
            item.save()
        return redirect('order_detail', my_order.pk)
    except:
        return redirect('cart_items')


def apply_coupon(request):
    if request.method == 'POST':
        my_order = Order.objects.get(id=request.POST['order_id'])
        try:
            my_discount = BonusDiscount.objects.get(coupon=request.POST['coupon'])
            my_order.discount_code = request.POST['coupon']
            my_order.save()
        except:
            messages.error(request, 'کد تخفیف اشتباه است')
    return redirect('order_detail', request.POST['order_id'])


def final_submit(request, pk):
    my_order = Order.objects.get(id=pk)
    my_order.status = 'ثبت شده'
    my_order.save()
    return redirect('order_detail', pk)
