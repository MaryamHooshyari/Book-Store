from django.views.generic import ListView, DetailView
from ..models.book import Book


class BookList(ListView):
    model = Book
    template_name = 'book/list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'book/detail.html'
