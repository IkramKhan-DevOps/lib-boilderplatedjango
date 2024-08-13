# SPACE HOLDER MIXINS
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
class StaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden("You must be a staff member to access this page.")
        return super().handle_no_permission()




class CustomPermissionMixin(UserPassesTestMixin):
    permission_required = None

    def test_func(self):
        if self.permission_required:
            return self.request.user.has_perm(self.permission_required)
        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().handle_no_permission()
