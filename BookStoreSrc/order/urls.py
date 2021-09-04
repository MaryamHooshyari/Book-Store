from django.urls import path

from .views import CartItems, OrderItemList, cart_add

urlpatterns = [
    path('add-item/', cart_add, name='add_cart_item')
    # path('cart/', CartItems.as_view(), name='cart_items'),
    # path('', cart_add, name='cart_add')
]

urlpatterns += [
    path('order/detail/<int:pk>', OrderItemList.as_view(), name='order_detail'),
]
