from accounts.permissions import UserAccessMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from ..forms.category import CategoryCreateForm, CategoryUpdateForm
from ..models.category import Category


# staff panel
class StaffCategory(ListView):
    model = Category
    template_name = 'category/staff_category.html'


class StaffCategoryDetail(DetailView):
    model = Category
    template_name = 'category/staff_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['books'] = context['category'].book_category.all()
        return context


class CategoryCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'product.add_category'

    form_class = CategoryCreateForm
    model = Category
    template_name = 'category/create.html'
    success_url = reverse_lazy('staff_category')


class CategoryUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'product.change_category'

    form_class = CategoryUpdateForm
    model = Category
    template_name = 'category/edit.html'
    success_url = reverse_lazy('staff_category')


class CategoryDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'product.delete_category'

    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('staff_category')


# customer panel
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
