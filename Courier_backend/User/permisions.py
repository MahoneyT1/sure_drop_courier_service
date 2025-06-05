from rest_framework.permissions import BasePermission


class isCourier(BasePermission):
    """Permisson for users """

    def has_permision(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Courier'