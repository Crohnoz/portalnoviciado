from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite editar sólo si el usuario es el dueño del objeto.
    """

    def has_object_permission(self, request, view, obj):
        # Lectura (GET, HEAD, OPTIONS) siempre permitida
        if request.method in permissions.SAFE_METHODS:
            return True

        # Escribir solo si el usuario es el dueño
        return obj.usuario == request.user or request.user.is_staff  # staff opcional
