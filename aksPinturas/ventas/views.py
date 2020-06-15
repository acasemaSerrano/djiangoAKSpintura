from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Factura
from django.urls import reverse, reverse_lazy

class FacturaList(ListView):
    model = Factura
    template_name = "ventas/factura_list.html"



class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'ventas/factura_view.html'


