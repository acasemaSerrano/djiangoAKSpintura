from django.contrib import admin
from .models import Factura, FacturaLinea
# Register your models here.



class FacturaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'date')

class FacturaLineaAdmin(admin.ModelAdmin):
    list_display = ('FacturaPerteneciente_id','produtos_id','cantidad')


admin.site.register(Factura, FacturaAdmin)
admin.site.register(FacturaLinea, FacturaLineaAdmin)