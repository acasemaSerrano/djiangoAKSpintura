from django.urls import path
from . import views

urlpatterns = [
    path('', views.FacturaList.as_view(), name="factura_list"),
    path('view/<pk>', views.FacturaDetailView.as_view(), name="factura_view"),
]