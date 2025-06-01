from django.shortcuts import redirect
from django.contrib import messages

def user_type_required(required_type):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not hasattr(request.user, 'userprofile') or request.user.userprofile.user_type != required_type:
                messages.error(request, 'Access denied.')
                return redirect('accounts:login')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator 