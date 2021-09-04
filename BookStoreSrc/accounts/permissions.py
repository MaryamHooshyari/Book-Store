from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
# from rest_framework import permissions
# from rest_framework.permissions import BasePermission


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('403_page')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

#
# class IsOwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # read only permission
#         if request.method in permissions.SAFE_METHODS:  # safe methods are (get, head, )
#             return True
#         # update and delete permission for owner
#         return request.user == obj.owner
