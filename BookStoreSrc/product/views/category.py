from django.views.generic import DetailView, ListView

from ..models.category import Category


class CategoryList(ListView):
    model = Category
    template_name = 'category/list.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['books'] = context['category'].book_category.all()
        return context
