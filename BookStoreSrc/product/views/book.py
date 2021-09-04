from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from ..forms.book import BookCreateForm, BookUpdateForm
from ..models.book import Book
from accounts.permissions import UserAccessMixin


# staff panel
class BookCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'product.add_book'

    form_class = BookCreateForm
    model = Book
    template_name = 'book/create.html'
    success_url = reverse_lazy('staff_home')


class BookUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'product.change_book'

    form_class = BookUpdateForm
    model = Book
    template_name = 'book/edit.html'
    success_url = reverse_lazy('staff_home')


class BookDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'product.delete_book'

    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('staff_home')


# customer panel
class BookList(ListView):
    model = Book
    template_name = 'book/list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'book/detail.html'
