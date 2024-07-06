from django.urls import path
from .views import AdepacRegView, AdepacHomeClienteView




app_name="adepac"

urlpatterns=[
    path('', AdepacRegView.as_view(), name="registro"),

    path('', AdepacHomeClienteView.as_view(), name="homecliente")
]