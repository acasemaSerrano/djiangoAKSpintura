from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import clientes
from .forms import clientesForm

def client_list(request):
    return render(request, "clientes/client_list.html")

def client_create(request):
    return render(request, "clientes/client_create.html")

def client_edit(request):
    return render(request, "clientes/client_edit.html")



class ClienteList(ListView):
    model = clientes
    template_name = "clientes/client_list.html"

class ClienteCreate(CreateView):
    model = clientes
    form_class = clientesForm
    #fields = ['profile_image','name','surname','phone','country','is_company','is_blacklisted','is_employee','is_supplier','is_active',]
    template_name = 'clientes/client_create.html'
    success_url = reverse_lazy('client_list')

class ClienteEdit(UpdateView):
    model = clientes
    form_class = clientesForm
    template_name = "clientes/client_edit.html"
    success_url = reverse_lazy('client_list')


class ClientestDelete(DeleteView):
    model = clientes
    template_name = "clientes/client_delete.html"
    success_url = reverse_lazy('client_list')