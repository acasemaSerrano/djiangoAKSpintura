from django.db import models
from productos.models import Product
from clientes.models import clientes
from datetime import datetime



class Factura(models.Model):
    cliente = models.ForeignKey(
        clientes,
        verbose_name = "cliente", 
        blank = False,
        null = False,
        on_delete = models.CASCADE,
        )
    date = models.DateTimeField(default=datetime.now(), auto_now_add=False, verbose_name="Fecha emmitida")
    class Meta:
        verbose_name = "factura"
        verbose_name_plural = "facturas"

class FacturaLinea(models.Model):
    FacturaPerteneciente_id =  models.ForeignKey(
        Factura,
        verbose_name = "lista De producto",
        blank = False,
        null = False,
        on_delete = models.CASCADE,
        )
    produtos_id = models.ForeignKey(
        Product,
        verbose_name = "lista De producto",
        blank = False,
        null = False,
        on_delete = models.CASCADE,
        )
    cantidad = models.IntegerField(verbose_name="cantidad")
    class Meta:
        verbose_name = "linea de factura"
        verbose_name_plural = "lineas de facturas"

