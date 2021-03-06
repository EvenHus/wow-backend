from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit there own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user if trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id


class PostNewImage(permissions.BasePermission):
    """Allow the user to post new image."""

    def has_object_permission(self, request, view, obj):
        """Checks if the user if trying to post a new image using their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
