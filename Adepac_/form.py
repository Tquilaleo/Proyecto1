from django import forms

from .models import Cliente,  Producto, ItemCarrito

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields= ( 'rut', 'nombre_cl', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'contrasena'
)