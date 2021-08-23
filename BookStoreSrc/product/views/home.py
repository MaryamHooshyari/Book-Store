from django.views.generic import ListView

from ..models.book import Book


class HomeView(ListView):
    model = Book
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # todo: have to change this query to more sold books
        context['more_sold'] = self.model.objects.all().order_by('id')[:4]
        context['fresh'] = self.model.objects.all().order_by('-created')[:4]
        return context
