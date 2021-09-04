from accounts.permissions import UserAccessMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from ..forms.author import AuthorCreateForm, AuthorUpdateForm
from ..models.author import Author


# staff panel
class StaffAuthor(ListView):
    model = Author
    template_name = 'author/staff_author.html'


class StaffAuthorDetail(DetailView):
    model = Author
    template_name = 'author/staff_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['books'] = context['author'].book_author.all()
        return context


class AuthorCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'product.add_author'

    form_class = AuthorCreateForm
    model = Author
    template_name = 'author/create.html'
    success_url = reverse_lazy('staff_author')


class AuthorUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'product.change_author'

    form_class = AuthorUpdateForm
    model = Author
    template_name = 'author/edit.html'
    success_url = reverse_lazy('staff_author')


class AuthorDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'product.delete_author'

    model = Author
    template_name = 'author/delete.html'
    success_url = reverse_lazy('staff_author')


# customer panel
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
