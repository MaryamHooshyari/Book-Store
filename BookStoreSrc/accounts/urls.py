from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views import SignUpView, StaffHome, login_redirect

urlpatterns = [
    path('login_redirect/', login_redirect, name='login_redirect'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

urlpatterns += [
    path('admin-panel/', TemplateView.as_view(template_name='admin/admin_panel.html'), name='admin_panel'),
    path('admin-panel/django-admin/', admin.site.urls),
    path('admin-panel/report/', TemplateView.as_view(template_name='admin/admin_report.html'), name='admin_report'),
]

urlpatterns += [
    path('staff/', StaffHome.as_view(), name='staff_home'),
]
