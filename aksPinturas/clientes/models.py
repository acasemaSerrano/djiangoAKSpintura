from django.db import models

class Country(models.Model):
  country_name = models.CharField(max_length=200, verbose_name="Nombre del País")
  
  class Meta:
    verbose_name = "País"
    verbose_name_plural = "Paises"

  def __str__(self):
    return self.country_name

class clientes(models.Model):
  profile_image = models.ImageField(verbose_name="Foto de Perfil", null=True, blank=True, upload_to="Clientes")
  name = models.CharField(max_length=200, verbose_name="Nombre")
  surname = models.CharField(max_length=200, verbose_name="Apellidos")
  phone = models.CharField(max_length=9, verbose_name="Telefono")
  country = models.ForeignKey(
    Country,
    verbose_name = "País", 
    blank = True,
    null = True,
    on_delete = models.SET_NULL,
    )
   
  is_company = models.BooleanField(null=True, blank=True, verbose_name="Compañia")
  is_blacklisted = models.BooleanField(null=True, blank=True, verbose_name="Lista Negra")
  is_active = models.BooleanField(null=True, blank=True, verbose_name="Activo")
  is_supplier = models.BooleanField(null=True, blank=True, verbose_name="Proveedor")
  is_employee = models.BooleanField(null=True, blank=True, verbose_name="Empleado")


  class Meta:
    verbose_name = "Contacto"
    verbose_name_plural = "Contactos"

  def __str__(self):
    cadena = self.name + " , " + self.surname
    return cadena