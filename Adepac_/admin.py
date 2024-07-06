from django.contrib import admin

from .models import Cliente, Producto, Carrito,ItemCarrito


admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)

