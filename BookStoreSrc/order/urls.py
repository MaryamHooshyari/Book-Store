from django.urls import path

from .views import CartItems, cart_add

urlpatterns = [
    path('cart/', CartItems.as_view(), name='cart_items'),
    path('', cart_add, name='cart_add')
]
