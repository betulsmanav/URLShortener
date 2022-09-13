from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsUserRead(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # check if user is owner
        return request.user == obj.user