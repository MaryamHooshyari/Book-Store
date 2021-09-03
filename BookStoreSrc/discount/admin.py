from django.contrib import admin

from .models import BonusDiscount, BookDiscount


@admin.register(BookDiscount)
class BookDiscountAdmin(admin.ModelAdmin):
    fields = ('book', ('start_date', 'expire_date'), ('amount', 'percent'))
    list_display = ['book', 'start_date', 'expire_date', 'amount', 'percent', 'discount_price']
    list_editable = ['amount', 'percent']
    ordering = ['-start_date', 'expire_date']


@admin.register(BonusDiscount)
class BonusDiscountAdmin(admin.ModelAdmin):
    fields = ('coupon', ('start_date', 'expire_date'), ('amount', 'percent'), 'limited_count', 'is_active')
    list_display = ['coupon', 'start_date', 'expire_date', 'amount', 'percent', 'limited_count', 'is_active']
    list_editable = ['amount', 'percent', 'limited_count']
    ordering = ['-start_date', 'expire_date']
