from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from product.models.book import Book

from .forms import CustomUserCreationForm


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
