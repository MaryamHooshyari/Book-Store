from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from product.models.book import Book
from ..forms import StaffCreationForm, StaffChangeForm

from ..models import Employee


class StaffCreate(CreateView):
    form_class = StaffCreationForm
    model = Employee
    template_name = 'employee/create.html'
    success_url = reverse_lazy('staff_list')


class StaffUpdate(UpdateView):
    form_class = StaffChangeForm
    model = Employee
    template_name = 'employee/edit.html'
    success_url = reverse_lazy('staff_list')


class StaffDelete(DeleteView):
    model = Employee
    template_name = 'employee/delete.html'
    success_url = reverse_lazy('staff_list')


class StaffList(ListView):
    model = Employee
    template_name = 'employee/staff_list.html'
    queryset = model.objects.filter(is_staff=True).filter(is_superuser=False)


class StaffHome(ListView):
    model = Book
    template_name = 'employee/staff_home.html'
