from django.views.generic import ListView, DetailView
from ..models.author import Author
from ..models.book import Book


class AuthorList(ListView):
    model = Author
    template_name = 'author/list.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author/detail.html'
    # query = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.query
        context['author'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        return context
