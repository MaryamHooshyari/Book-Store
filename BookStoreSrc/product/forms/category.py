from django import forms
from django.utils.translation import gettext_lazy as _
from product.models.category import Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        labels = {
            'name': _('نام'),
            'slug': _('اسلاگ')
        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        labels = {
            'name': _('نام'),
            'slug': _('اسلاگ')
        }
