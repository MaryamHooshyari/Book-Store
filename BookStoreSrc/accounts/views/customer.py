from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from ..forms import CustomUserChangeForm, AddressForm
from ..models import Customer, Address


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
class AddressCreate(CreateView):
    form_class = AddressForm
    model = Address
    template_name = 'customer/address_create.html'
    success_url = reverse_lazy('home')


class AddressUpdate(UpdateView):
    form_class = AddressForm
    model = Address
    template_name = 'customer/address_edit.html'
    success_url = reverse_lazy('home')


class AddressDelete(DeleteView):
    model = Address
    template_name = 'customer/address_delete.html'
    success_url = reverse_lazy('home')
