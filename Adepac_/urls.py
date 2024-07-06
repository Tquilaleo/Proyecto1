from django.urls import path
from . views import AdepacRegView, AdepacHomeClienteView
from . import views


app_name="adepac"

urlpatterns=[
    path('', AdepacRegView.as_view(), name="registro"),
     path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:itemcarrito_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    
    path('', AdepacHomeClienteView.as_view(), name="homecliente"),
   
]