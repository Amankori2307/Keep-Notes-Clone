from rest_framework.permissions import BasePermission

class NotesPermission(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        user = request.user
        if method in ["GET", "POST"]:
            return user.is_authenticated



class LabelPermission(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        user = request.user
        if method in ["GET", "POST"]:
            return user.is_authenticated