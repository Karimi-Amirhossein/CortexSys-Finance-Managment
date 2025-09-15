from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Permission to allow only the owner of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return True if the requesting user is the owner of the object.
        """
        return obj.user == request.user
