from django.db.models import Q
from django.views.generic import ListView

from ..models.author import Author
from ..models.book import Book
from ..models.category import Category


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.request.GET.get("searchbar")
        context['books'] = self.model.objects.filter(Q(title__icontains=key))
        context['authors'] = Author.objects.filter(Q(first_name__icontains=key) | Q(last_name__icontains=key))
        context['categories'] = Category.objects.filter(Q(name__icontains=key))
        return context
