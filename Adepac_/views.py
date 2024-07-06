from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .form import PostCreateForm
from .models import Cliente

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