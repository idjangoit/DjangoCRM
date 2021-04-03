from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organizor"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizor:
            #return self.handle_no_permission()
            return redirect('leads:lead-list')
        return super().dispatch(request, *args, **kwargs)
