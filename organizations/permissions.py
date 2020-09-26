from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import Owner

class HasOrganizationPermissions(BasePermission):

    def has_permission(self, request, view):
        return request.user.user_type == "Owner"

class HasOrganizationLocationPermissions(BasePermission):

    def has_permission(self, request, view):
        return (request.user.user_type == "Owner" or request.user.user_type == "Executive")

class HasLocationBranchesPermissions(BasePermission):

    def has_permission(self, request, view):
        return (request.user.user_type == "Owner" or request.user.user_type == "Executive")

# class IsAllowedToWrite(BasePermission):
    
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True

#         return request.user.user_type == "Owner"

# class IsAllowedToRead(BasePermission):
    
#     def has_object_permission(self, request, view, obj):
#         return obj.is_allowed_to_read == "YES"