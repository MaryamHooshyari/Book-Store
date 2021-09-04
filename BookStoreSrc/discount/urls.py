from django.urls import path

from .views import *

urlpatterns = [
    # book discount
    path('book-discount/all/', BookDiscountList.as_view(), name='book_discount_list'),
    path('book-discount/create/', BookDiscountCreate.as_view(), name='book_discount_create'),
    path('book-discount/edit/<int:pk>', BookDiscountUpdate.as_view(), name='book_discount_edit'),
    path('book-discount/delete/<int:pk>', BookDiscountDelete.as_view(), name='book_discount_delete'),

    # bonus discount
    path('bonus-discount/all/', BonusDiscountList.as_view(), name='bonus_discount_list'),
    path('bonus-discount/all/customer-view/', BonusDiscountListCustomer.as_view(), name='bonus_discount_customer_view'),
    path('bonus-discount/create/', BonusDiscountCreate.as_view(), name='bonus_discount_create'),
    path('bonus-discount/edit/<int:pk>', BonusDiscountUpdate.as_view(), name='bonus_discount_edit'),
    path('bonus-discount/delete/<int:pk>', BonusDiscountDelete.as_view(), name='bonus_discount_delete'),
]
