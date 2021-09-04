from django import forms
from django.utils.translation import gettext_lazy as _

from .models import BonusDiscount, BookDiscount


class BookDiscountCreateForm(forms.ModelForm):
    class Meta:
        model = BookDiscount
        fields = ['book', 'start_date', 'expire_date', 'amount', 'percent']
        labels = {
            'book': _('کتاب'),
            'start_date': _('تاریخ شروع'),
            'expire_date': _('تاریخ انقضا'),
            'amount': _('تخفیف نقدی'),
            'percent': _('تخفیف درصدی'),
        }


class BookDiscountUpdateForm(forms.ModelForm):
    class Meta:
        model = BookDiscount
        fields = ['start_date', 'expire_date', 'amount', 'percent']
        labels = {
            'start_date': _('تاریخ شروع'),
            'expire_date': _('تاریخ انقضا'),
            'amount': _('تخفیف نقدی'),
            'percent': _('تخفیف درصدی'),
        }


class BonusDiscountCreateForm(forms.ModelForm):
    class Meta:
        model = BonusDiscount
        fields = ['coupon', 'start_date', 'expire_date', 'amount', 'percent', 'limited_count']
        labels = {
            'coupon': _('کد تخفیف'),
            'start_date': _('تاریخ شروع'),
            'expire_date': _('تاریخ انقضا'),
            'amount': _('مبلغ ماکسیموم'),
            'percent': _('درصد تخفیف'),
            'limited_count': _('تعداد استفاده مجاز')
        }


class BonusDiscountUpdateForm(forms.ModelForm):
    class Meta:
        model = BonusDiscount
        fields = ['coupon', 'start_date', 'expire_date', 'amount', 'percent', 'limited_count', 'is_active']
        labels = {
            'coupon': _('کد تخفیف'),
            'start_date': _('تاریخ شروع'),
            'expire_date': _('تاریخ انقضا'),
            'amount': _('مبلغ ماکسیموم'),
            'percent': _('درصد تخفیف'),
            'limited_count': _('تعداد استفاده مجاز'),
            'is_active': _('فعال')
        }
