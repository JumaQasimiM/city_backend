from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    message = "You do not have permission to perform this action."
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS → all have permision --> this is for viewer user
        if request.method in SAFE_METHODS:
            return True

        # only admin
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role == "admin"
        )

    
class IsAdminBusinessOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # GET برای همه (حتی بدون login)
        if request.method in SAFE_METHODS:
            return True

        # بقیه فقط با login
        if not request.user or not request.user.is_authenticated:
            return False

        return request.user.role in ['admin', 'business']