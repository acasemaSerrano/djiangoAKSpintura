from django.db import models

class Category(models.Model):
  category_name = models.CharField(max_length=200, verbose_name="Nombre categoria")

  class Meta:
    verbose_name = "Categoria"
    verbose_name_plural = "Categorias"

  def __str__(self):
    return self.category_name



class Product(models.Model):
  product_image = models.ImageField(verbose_name="Foto de Producto", null=True, blank=True, upload_to="Productos")
  name = models.CharField(max_length=200, verbose_name="Nombre")
  code = models.CharField(max_length=200, verbose_name="Codigo del producto")
  description = models.TextField(verbose_name="Descripcion del producto")
  list_price = models.DecimalField(verbose_name="Precio del producto", max_digits=19, decimal_places=2)
  
  category = models.ForeignKey(
       Category,
       verbose_name = "Categoria del producto", 
       blank = True,
       null = True,
       on_delete = models.CASCADE,
       )
  quantity = models.IntegerField(verbose_name="cantidad")

  class Meta:
    verbose_name = "Producto"
    verbose_name_plural = "Productos"

  def __str__(self):
    return self.name


