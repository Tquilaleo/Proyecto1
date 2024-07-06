from django.contrib import admin

from .models import Cliente, Producto, ItemCarrito


admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(ItemCarrito)


