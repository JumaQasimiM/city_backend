from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"


class IsBusiness(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "business"


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == "admin" or obj.owner == request.user
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS