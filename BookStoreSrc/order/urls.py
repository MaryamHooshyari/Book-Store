from django.urls import path

from .views import CartItems, OrderItemList, cart_add, in_cart_add, order_item_delete,submit_order, apply_coupon,final_submit, apply_address

urlpatterns = [
    path('add-item/', cart_add, name='add_cart_item'),
    path('in_cart_add', in_cart_add, name='in_cart_add'),
    path('cart/', CartItems.as_view(), name='cart_items'),
    path('order-item-delete/<int:pk>', order_item_delete, name='order_item_delete'),
    path('submit-order/', submit_order, name='submit_order'),
    path('apply-coupon/', apply_coupon, name='apply_coupon'),
    path('final-submit/<int:pk>', final_submit, name='final_submit'),
    path('order/apply-address/', apply_address, name='apply_address')
    # path('', cart_add, name='cart_add')
]

urlpatterns += [
    path('order/detail/<int:pk>', OrderItemList.as_view(), name='order_detail'),
]
