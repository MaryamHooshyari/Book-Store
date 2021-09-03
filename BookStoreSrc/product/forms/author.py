from django import forms
from django.utils.translation import gettext_lazy as _
from product.models.author import Author


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'slug']
        labels = {
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'slug': _('اسلاگ')
        }


class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'slug']
        labels = {
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'slug': _('اسلاگ')
        }
