from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre_cl = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)  
    contrasena = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return f"{self.nombre_cl} {self.apellido_paterno}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"