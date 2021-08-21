from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Customer, CustomUser, Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('slug',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'is_staff', 'is_active')}),
    )


class EmployeeAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        return CustomUser.objects.filter(is_staff=True).filter(is_superuser=False)


class CustomerAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        return CustomUser.objects.filter(is_staff=False).filter(is_superuser=False)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
