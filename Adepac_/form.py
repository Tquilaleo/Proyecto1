from django import forms
from .models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre_cl', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'contrasena']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_prod', 'descripcion', 'precio', 'stock']
