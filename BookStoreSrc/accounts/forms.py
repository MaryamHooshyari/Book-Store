from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Address, CustomUser


# custom user
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)
        labels = {
            'email': _('رایانامه')
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'email': _('رایانامه')
        }


# staff
class StaffCreationForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm):
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields + ('first_name', 'last_name', 'is_staff')
        labels = {
            'email': _('رایانامه')
        }


class StaffChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active')
        labels = {
            'email': _('رایانامه')
        }


# address
class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('state', 'city', 'town', 'street', 'postal_code', 'details', 'is_default')
        labels = {
            'state': _('استان'),
            'city': _('شهر'),
            'town': _('محله'),
            'street': _('خیابان'),
            'postal_code': _('کد پستی'),
            'details': _('جزییات'),
            'is_default': _('آدرس اصلی'),
        }
