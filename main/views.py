from rest_framework import viewsets
from .models import Categoria, Negocio, Producto
from .serializers import CategoriaSerializer, NegocioSerializer, ProductoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Producto, ImagenProducto
from .serializers import ImagenProductoSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def subir_imagen_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        if producto.usuario != request.user and not request.user.is_staff:
            return Response({'detail': 'No autorizado.'}, status=403)
    except Producto.DoesNotExist:
        return Response({'detail': 'Producto no encontrado.'}, status=404)

    serializer = ImagenProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(producto=producto)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
