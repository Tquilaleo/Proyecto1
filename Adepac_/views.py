from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .form import PostCreateForm
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class AdepacHomeClienteView(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'HomeCliente.html', context)
    
class AdepacRegView(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'RegistroCliente.html', context)
    

class AdepacReg_CreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'RegistroCliente.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                rut = form.cleaned_data.get('rut')
                nombre_cl = form.cleaned_data.get('nombre_cl')
                apellido_paterno = form.cleaned_data.get('apellido_paterno')
                apellido_materno = form.cleaned_data.get('apellido_materno')
                fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
                telefono = form.cleaned_data.get('telefono')
                email = form.cleaned_data.get('email')
                direccion = form.cleaned_data.get('direccion')
                contrasena = form.cleaned_data.get('contrasena')

                p, created = Cliente.objects.get_object_or_create(
                    rut=rut,
                    nombre_cl=nombre_cl,
                    apellido_paterno=apellido_paterno,
                    apellido_materno=apellido_materno,
                    fecha_nacimiento=fecha_nacimiento,
                    telefono=telefono,
                    email=email,
                    direccion=direccion,
                    contrasena=contrasena
                )

                p.save()
                return redirect('adepac:homecliente')

        context={
            
        }
        return render(request, 'RegistroCliente.html', context)
    


class AdepacHomeClienteView(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'HomeCliente.html', context)
    
@method_decorator(login_required, name='dispatch')
class AgregarAlCarritoView(View):
    def post(self, request, product_id, *args, **kwargs):
        producto = get_object_or_404(Producto, id_producto=product_id)
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=usuario)

        item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        if not created:
            item_carrito.cantidad += 1
            item_carrito.save()

        return redirect('ver_carrito')

@method_decorator(login_required, name='dispatch')
class VerCarritoView(View):
    def get(self, request, *args, **kwargs):
        carrito = get_object_or_404(Carrito, usuario=request.user)
        items_carrito = ItemCarrito.objects.filter(carrito=carrito)
        precio_total = sum(item.subtotal() for item in items_carrito)
        context = {
            'items_carrito': items_carrito,
            'precio_total': precio_total
        }
        return render(request, 'Carrito.html', context)

@method_decorator(login_required, name='dispatch')
class ActualizarCarritoView(View):
    def post(self, request, item_id, *args, **kwargs):
        item_carrito = get_object_or_404(ItemCarrito, id=item_id)
        if 'cantidad' in request.POST:
            item_carrito.cantidad = request.POST['cantidad']
            item_carrito.save()

        return redirect('ver_carrito')

@method_decorator(login_required, name='dispatch')
class EliminarDelCarritoView(View):
    def post(self, request, item_id, *args, **kwargs):
        item_carrito = get_object_or_404(ItemCarrito, id=item_id)
        item_carrito.delete()
        return redirect('ver_carrito')    