from rest_framework.permissions import BasePermission

class NotesPermission(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        user = request.user
        if method == "GET":
            return user.is_authenticated