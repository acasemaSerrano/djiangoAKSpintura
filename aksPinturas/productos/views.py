from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Product
from .forms import ProductForm

def product_list(request):
    return render(request, "productos/product_list.html")

def product_create(request):
    return render(request, "productos/product_create.html")

def product_edit(request):
    return render(request, "productos/product_edit.html")




class ProductList(ListView):
    model = Product
    template_name = "productos/product_list.html"


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'productos/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductEdit(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "productos/product_edit.html"
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = "productos/product_delete.html"
    success_url = reverse_lazy('product_list')
