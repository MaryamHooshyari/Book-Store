from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order.models import Order
from product.models.book import Book

from .forms import CustomUserCreationForm
from .models import Address, Customer


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def login_redirect(request):
    if request.user.is_superuser:
        return redirect('admin_panel')
    elif request.user.is_staff:
        return redirect('staff_home')
    else:
        return redirect('home')


class StaffHome(ListView):
    model = Book
    template_name = 'employee/staff_home.html'


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer/detail.html'


class AddressList(DetailView):
    model = Customer
    template_name = 'customer/address_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['addresses'] = context['user'].address.all()
        return context


class OrderList(DetailView):
    model = Customer
    template_name = 'customer/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['orders'] = context['user'].orders.all()
        return context
