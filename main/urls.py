from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, NegocioViewSet, ProductoViewSet, RegisterUserView
from .views import subir_imagen_producto
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Router para viewsets (API de recursos)
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'negocios', NegocioViewSet)
router.register(r'productos', ProductoViewSet)

# URLs disponibles bajo /api/
urlpatterns = [
    path('', include(router.urls)),

    # 🔐 Autenticación JWT
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ Registro de usuario
    path('register/', RegisterUserView.as_view(), name='user-register'),
]

urlpatterns += [
    path('productos/<int:producto_id>/imagenes/', subir_imagen_producto, name='subir-imagen-producto'),
]