from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Categoria, Negocio, Producto, ImagenProducto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = '__all__'

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = ['id', 'imagen_url','imagen']
        
    def get_imagen_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.imagen.url)
        return obj.imagen.url

class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenProductoSerializer(many=True, read_only=True)
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    negocio = serializers.PrimaryKeyRelatedField(queryset=Negocio.objects.all())

    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ['usuario']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user