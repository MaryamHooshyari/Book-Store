from django.contrib import admin

from .models import BonusDiscount, BookDiscount


@admin.register(BookDiscount)
class BookDiscountAdmin(admin.ModelAdmin):
    list_display = ['book', 'start_date', 'expire_date', 'amount', 'percent', 'discount_price']
    list_editable = ['amount', 'percent']


@admin.register(BonusDiscount)
class BonusDiscountAdmin(admin.ModelAdmin):
    list_display = ['coupon', 'start_date', 'expire_date', 'amount', 'percent', 'is_active']
    list_editable = ['amount', 'percent']
