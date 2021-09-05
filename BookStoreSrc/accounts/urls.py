from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views.all_user_related import login_redirect, signup, activate
from .views.customer import (AddressCreate, AddressCreateInOrder, AddressDelete, AddressList,
                             AddressUpdate, CustomerDelete, CustomerDetail,
                             CustomerList, CustomerUpdate, OrderList)
from .views.employee import (StaffCreate, StaffDelete, StaffHome, StaffList,
                             StaffUpdate)

# all users
urlpatterns = [
    path('user/forbidden/', TemplateView.as_view(template_name='403_page.html'), name='403_page'),
    path('login_redirect/', login_redirect, name='login_redirect'),
    path('signup/user/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]

# admin
urlpatterns += [
    path('admin/django-admin/', admin.site.urls),
    path('admin/report/', TemplateView.as_view(template_name='admin/admin_report.html'), name='admin_report'),
]

# staff
urlpatterns += [
    path('staff/', StaffHome.as_view(), name='staff_home'),
    path('staff/all/', StaffList.as_view(), name='staff_list'),
    path('staff/create/', StaffCreate.as_view(), name='staff_create'),
    path('staff/edit/<int:pk>', StaffUpdate.as_view(), name='staff_edit'),
    path('staff/delete/<int:pk>', StaffDelete.as_view(), name='staff_delete'),
]

# customer
urlpatterns += [
    path('customer/<slug>', CustomerDetail.as_view(), name='user_detail'),
    path('customer/<slug>/addresses/', AddressList.as_view(), name='address_list'),
    path('customer/order/add-address/', AddressCreateInOrder.as_view(), name='address_in_order'),
    path('customer/<slug>/addresses/create/', AddressCreate.as_view(), name='address_create'),
    path('customer/<slug>/addresses/edit/<int:pk>', AddressUpdate.as_view(), name='address_edit'),
    path('customer/<slug>/addresses/delete/<int:pk>', AddressDelete.as_view(), name='address_delete'),
    path('customer/<slug>/orders/', OrderList.as_view(), name='order_list'),
    path('customer/all/', CustomerList.as_view(), name='customer_list'),
    path('customer/<slug>/edit/', CustomerUpdate.as_view(), name='customer_edit'),
    path('customer/<slug>/delete/', CustomerDelete.as_view(), name='customer_delete'),
]
