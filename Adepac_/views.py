from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Producto, Cliente, Carrito, ItemCarrito
from .form import ClienteForm, ProductoForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Vistas relacionadas con la autenticación y el perfil del usuario

def index(request):
    return render(request, 'Adepac_/index.html')

def login_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'Adepac_/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'Adepac_/login.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'Adepac_/registro.html', {'form': form})

@login_required
def logout_sesion(request):
    logout(request)
    return redirect('index')

@login_required
def perfil(request):
    user = request.user
    cliente = Cliente.objects.get(user=user)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'Adepac_/perfil.html', {'form': form})

# Vistas relacionadas con los productos y el carrito de compras

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Adepac_/lista_productos.html', {'productos': productos})

@login_required
def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'Adepac_/detalle_producto.html', {'producto': producto})

@login_required
def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'Adepac_/agregar_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Adepac_/editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'Adepac_/eliminar_producto.html', {'producto': producto})

@login_required
def agregar_carrito(request, pk):
    producto = Producto.objects.get(pk=pk)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    if request.method == "POST":
        cantidad = int(request.POST.get('cantidad', 1))
        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto, defaults={'cantidad': cantidad})
        if not created:
            item.cantidad += cantidad
            item.save()
        return redirect('ver_carrito')
    return render(request, 'Adepac_/agregar_carrito.html', {'producto': producto})

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = carrito.items.all()
    return render(request, 'Adepac_/ver_carrito.html', {'items': items})

@login_required
def eliminar_item_carrito(request, pk):
    item = ItemCarrito.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('ver_carrito')
    return render(request, 'Adepac_/eliminar_item_carrito.html', {'item': item})
