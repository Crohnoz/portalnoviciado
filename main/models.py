from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Negocio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    destacado = models.BooleanField(default=False)  # Promoción pagada
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return f"Imagen de {self.producto.titulo}"

usuario = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
        return self.titulo
