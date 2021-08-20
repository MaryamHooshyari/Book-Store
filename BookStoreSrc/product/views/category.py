from django.views.generic import ListView, DetailView
from ..models.category import Category


class CategoryList(ListView):
    model = Category
    template_name = 'category/list.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category/detail.html'
