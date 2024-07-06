from django.urls import path
from . import views

app_name = 'Adepac_'  

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_sesion, name='login'),
    path('logout/', views.logout_sesion, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('carrito/agregar/<int:pk>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<int:pk>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
]
