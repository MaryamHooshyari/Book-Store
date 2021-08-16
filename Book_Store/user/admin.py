from django.contrib import admin
from .models.accounts import CustomUser, Employee, Customer
from .models.address import Address


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('email', 'password', ('first_name', 'last_name'), 'username', 'groups', 'is_staff', 'is_active')
    # prepopulated_fields = {'slug': ('email',)}

    def get_queryset(self, request):
        return CustomUser.objects.filter(is_staff=True).filter(is_superuser=False)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('email', 'password', ('first_name', 'last_name'), 'username', 'groups', 'is_staff', 'is_active')
    # prepopulated_fields = {'slug': ('email',)}

    def get_queryset(self, request):
        return CustomUser.objects.filter(is_staff=False).filter(is_superuser=False)


admin.site.register(Address)
