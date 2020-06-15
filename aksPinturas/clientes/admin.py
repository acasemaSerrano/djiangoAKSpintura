from django.contrib import admin

from .models import clientes, Country

# Register your models here.
admin.site.register(clientes)
admin.site.register(Country)
