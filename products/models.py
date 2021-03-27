from django.db import models

# Create your models here.
class Product(models.Model):
    barcode = models.CharField(verbose_name="Código de barras", max_length=30)
    name = models.CharField(verbose_name="Producto", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Producto",
        verbose_name_plural= "Productos"
    
