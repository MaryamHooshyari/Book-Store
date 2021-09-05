from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.permissions import UserAccessMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from ..forms import AddressForm, CustomUserChangeForm
from ..models import Address, Customer
from order.models import Order


# for admin and staff
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


class CustomerUpdate(UpdateView):
    form_class = CustomUserChangeForm
    model = Customer
    template_name = 'customer/edit.html'

    def get_success_url(self):
        slug = self.request.user.slug
        return reverse_lazy('user_detail', kwargs={'slug': slug})


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customer/delete.html'
    success_url = reverse_lazy('home')


# address
class AddressCreate(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'accounts.add_address'

    form_class = AddressForm
    model = Address
    template_name = 'customer/address_create.html'

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.owner = request.user
            address.save()
            slug = self.request.user.slug
            return redirect('address_list', slug)
        else:
            messages.error(request, 'آدرس ثبت نشد:(')
            form = AddressForm()
            return render(request, 'customer/address_create.html', {'form': form})


class AddressUpdate(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'accounts.change_address'

    form_class = AddressForm
    model = Address
    template_name = 'customer/address_edit.html'

    def get_success_url(self):
        slug = self.request.user.slug
        return reverse_lazy('address_list', kwargs={'slug': slug})


class AddressDelete(UserAccessMixin, DeleteView):
    raise_exception = False
    permission_required = 'accounts.delete_address'

    model = Address
    template_name = 'customer/address_delete.html'

    def get_success_url(self):
        slug = self.request.user.slug
        return reverse_lazy('address_list', kwargs={'slug': slug})


# in_order
class AddressCreateInOrder(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'accounts.add_address'

    form_class = AddressForm
    model = Address
    template_name = 'customer/address_create.html'

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.owner = request.user
            address.save()
            order = Order.objects.get(owner=request.user, status='سفارش')
            return redirect('order_detail', order.pk)
        else:
            messages.error(request, 'آدرس ثبت نشد:(')
            form = AddressForm()
            return render(request, 'customer/address_create.html', {'form': form})
