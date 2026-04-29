from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS → all have permision 
        if request.method in SAFE_METHODS:
            return True

        # only admin
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role == "admin"
        )