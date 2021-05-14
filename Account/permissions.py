from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        return obj.account == request.user

class TeacherPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return True
    
    def has_object_permission(self, request, view, obj):
        return True