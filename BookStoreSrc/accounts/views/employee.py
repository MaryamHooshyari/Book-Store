from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from product.models.book import Book

from ..forms import StaffChangeForm, StaffCreationForm
from ..models import Employee


class StaffCreate(CreateView):
    form_class = StaffCreationForm
    model = Employee
    template_name = 'employee/create.html'

    def post(self, request, *args, **kwargs):
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            staff = form.save()
            staff.is_staff = True
            gp = Group.objects.get(name='دسترسی کارمند')
            staff.groups.add(gp)
            staff.save()
            return redirect('staff_list')
        else:
            messages.error(request, 'آدرس ثبت نشد:(')
            form = StaffCreationForm()
            return render(request, 'customer/address_create.html', {'form': form})


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
