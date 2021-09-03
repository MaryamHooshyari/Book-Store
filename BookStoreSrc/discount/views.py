from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *


# book discount
class BookDiscountList(ListView):
    model = BookDiscount
    template_name = 'book_discount/list.html'


class BookDiscountCreate(CreateView):
    form_class = BookDiscountCreateForm
    model = BookDiscount
    template_name = 'book_discount/create.html'
    success_url = reverse_lazy('book_discount_list')


class BookDiscountUpdate(UpdateView):
    form_class = BookDiscountUpdateForm
    model = BookDiscount
    template_name = 'book_discount/edit.html'
    success_url = reverse_lazy('book_discount_list')


class BookDiscountDelete(DeleteView):
    model = BookDiscount
    template_name = 'book_discount/delete.html'
    success_url = reverse_lazy('book_discount_list')


# bonus discount
class BonusDiscountList(ListView):
    model = BonusDiscount
    template_name = 'bonus_discount/list.html'


class BonusDiscountCreate(CreateView):
    form_class = BonusDiscountCreateForm
    model = BonusDiscount
    template_name = 'bonus_discount/create.html'
    success_url = reverse_lazy('bonus_discount_list')


class BonusDiscountUpdate(UpdateView):
    form_class = BonusDiscountUpdateForm
    model = BonusDiscount
    template_name = 'bonus_discount/edit.html'
    success_url = reverse_lazy('bonus_discount_list')


class BonusDiscountDelete(DeleteView):
    model = BonusDiscount
    template_name = 'bonus_discount/delete.html'
    success_url = reverse_lazy('bonus_discount_list')
