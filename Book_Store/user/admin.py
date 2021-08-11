from django.contrib import admin
from .models import Employee, Customer, Address


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'password', 'groups')


class CustomerAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'password', 'groups')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address)
