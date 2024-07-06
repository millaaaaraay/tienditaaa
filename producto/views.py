from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, ElementoCarrito

# Vistas existentes
def index(request):
    return render(request, 'pages/index.html')

def contacto(request):
    return render(request, 'pages/contacto.html')

def envios(request):
    return render(request, 'pages/envios.html')

def nosotros(request):
    return render(request, 'pages/nosotros.html')

def tienda(request):
    return render(request, 'pages/tienda.html')

# Nuevas vistas para el carrito de compras
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    elemento, created = ElementoCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    if not created:
        elemento.cantidad += 1
        elemento.save()

    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    elementos = ElementoCarrito.objects.filter(carrito=carrito)
    total = sum([elemento.total() for elemento in elementos])
    return render(request, 'pages/carrito.html', {'elementos': elementos, 'total': total})

@login_required
def eliminar_del_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('ver_carrito')
