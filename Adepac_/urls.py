from django.urls import path
from .views import AdepacRegView, AdepacHomeClienteView, AdepacReg_CreateView, AgregarAlCarritoView, VerCarritoView, ActualizarCarritoView, EliminarDelCarritoView

app_name = "adepac"

urlpatterns = [
    path('', AdepacRegView.as_view(), name="registro"),
    path('home/', AdepacHomeClienteView.as_view(), name="homecliente"),
    path('registro/crear/', AdepacReg_CreateView.as_view(), name='registro_crear'),
    path('agregar_al_carrito/<int:product_id>/', AgregarAlCarritoView.as_view(), name='agregar_al_carrito'),
    path('ver_carrito/', VerCarritoView.as_view(), name='ver_carrito'),
    path('actualizar_carrito/<int:item_id>/', ActualizarCarritoView.as_view(), name='actualizar_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', EliminarDelCarritoView.as_view(), name='eliminar_del_carrito'),
]
