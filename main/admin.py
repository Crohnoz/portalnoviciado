from django.contrib import admin
from .models import Categoria, Negocio, Producto, ImagenProducto

admin.site.register(Categoria)
admin.site.register(Negocio)
admin.site.register(Producto)
admin.site.register(ImagenProducto)
