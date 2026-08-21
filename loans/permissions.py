from rest_framework import permissions
from rest_framework.permissions import BasePermission

from accounts.models import CustomUser


class IsOwnerOrLibrarian(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.role == CustomUser.Role.LIBRARIAN:
            return True

        return obj.user == request.user