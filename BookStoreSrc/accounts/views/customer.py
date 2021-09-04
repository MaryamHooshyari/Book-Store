from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from ..forms import AddressForm, CustomUserChangeForm
from ..models import Address, Customer
from accounts.permissions import UserAccessMixin


# customer
class CustomerList(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    queryset = model.objects.filter(is_staff=False)


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer/detail.html'


class AddressList(DetailView):
    model = Customer
    template_name = 'customer/address_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['addresses'] = context['user'].address.all()
        return context


class OrderList(DetailView):
    model = Customer
    template_name = 'customer/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['orders'] = context['user'].orders.all()
        return context


# todo: reverse_lazy('user_detail')
class CustomerUpdate(UpdateView):
    form_class = CustomUserChangeForm
    model = Customer
    template_name = 'customer/edit.html'
    success_url = reverse_lazy('home')


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customer/delete.html'
    success_url = reverse_lazy('home')


# address
# todo: reverse_lazy('address_list')
class AddressCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'accounts.add_address'

    form_class = AddressForm
    model = Address
    template_name = 'customer/address_create.html'
    success_url = reverse_lazy('home')


class AddressUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'accounts.change_address'

    form_class = AddressForm
    model = Address
    template_name = 'customer/address_edit.html'
    success_url = reverse_lazy('home')


class AddressDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'accounts.delete_address'

    model = Address
    template_name = 'customer/address_delete.html'
    success_url = reverse_lazy('home')
