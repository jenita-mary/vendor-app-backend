from rest_framework.permissions import BasePermission


class IsVendorOwner(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):
        return (
            obj.vendor ==
            request.user.vendor_profile
        )