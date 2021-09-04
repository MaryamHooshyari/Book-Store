from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import *
from .models import *
from accounts.permissions import UserAccessMixin


# book discount
class BookDiscountList(UserAccessMixin, ListView):
    raise_exception = False
    permission_required = 'discount.view_bookdiscount'

    model = BookDiscount
    template_name = 'book_discount/list.html'


class BookDiscountCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'discount.add_bookdiscount'

    form_class = BookDiscountCreateForm
    model = BookDiscount
    template_name = 'book_discount/create.html'
    success_url = reverse_lazy('book_discount_list')


class BookDiscountUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'discount.change_bookdiscount'

    form_class = BookDiscountUpdateForm
    model = BookDiscount
    template_name = 'book_discount/edit.html'
    success_url = reverse_lazy('book_discount_list')


class BookDiscountDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'discount.delete_bookdiscount'

    model = BookDiscount
    template_name = 'book_discount/delete.html'
    success_url = reverse_lazy('book_discount_list')


# bonus discount
class BonusDiscountList(ListView):
    model = BonusDiscount
    template_name = 'bonus_discount/list.html'


class BonusDiscountListCustomer(ListView):
    model = BonusDiscount
    template_name = 'bonus_discount/customer_view.html'


class BonusDiscountCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'discount.add_bonusdiscount'

    form_class = BonusDiscountCreateForm
    model = BonusDiscount
    template_name = 'bonus_discount/create.html'
    success_url = reverse_lazy('bonus_discount_list')


class BonusDiscountUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'discount.change_bonusdiscount'

    form_class = BonusDiscountUpdateForm
    model = BonusDiscount
    template_name = 'bonus_discount/edit.html'
    success_url = reverse_lazy('bonus_discount_list')


class BonusDiscountDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'discount.delete_bonusdiscount'

    model = BonusDiscount
    template_name = 'bonus_discount/delete.html'
    success_url = reverse_lazy('bonus_discount_list')
