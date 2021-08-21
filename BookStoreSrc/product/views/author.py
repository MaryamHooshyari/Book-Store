from django.views.generic import DetailView, ListView

from ..models.author import Author


class AuthorList(ListView):
    model = Author
    template_name = 'author/list.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['books'] = context['author'].book_author.all()
        return context
