from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow user to update their own profile
    """

    def has_object_permission(self, request, view, obj):
        """Check users that want to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """
    Allow users to update their own status
    """
    def has_object_permission(self, request, view, obj):
        """
        Check the user that is trying to update his or her status

        Arguments:
            permissions {[type]} -- [description]
            request {[type]} -- [description]
            view {[type]} -- [description]
            obj {[type]} -- [description]
        """
        if request.method == permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
