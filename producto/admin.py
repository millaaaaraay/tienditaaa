from django.contrib import admin
from .models import Genero, Alumno, Producto, Categoria, Proveedor, Cliente, Pedido, Carrito, ElementoCarrito

# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(ElementoCarrito)
