from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'status', 'created', 'address', 'original_price', 'discount_code', 'final_price']
    ordering = ['-updated']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity', 'item_price']
    ordering = ['order', 'book']
