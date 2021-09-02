from django import forms
from product.models.book import Book
from django.utils.translation import gettext_lazy as _


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'categories', 'unit_price', 'number_in_stock', 'slug']
        labels = {
            'title': _('عنوان کتاب'),
            'authors': _('نویسنده ها'),
            'categories': _('دسته بندی ها'),
            'unit_price': _('قیمت واحد'),
            'number_in_stock': _('موجودی انبار'),
            'slug': _('اسلاگ')
        }


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'categories', 'unit_price', 'number_in_stock', 'slug']
        labels = {
            'title': _('عنوان کتاب'),
            'authors': _('نویسنده ها'),
            'categories': _('دسته بندی ها'),
            'unit_price': _('قیمت واحد'),
            'number_in_stock': _('موجودی انبار'),
            'slug': _('اسلاگ')
        }
