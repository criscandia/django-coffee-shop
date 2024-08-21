from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(
        max_length=200, verbose_name="nombre"
    )  # verbose_name es el nombre que se le asigna al campo en el admin
    description = models.TextField(max_length=300, verbose_name="descripción")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="precio"
    )  # Permite agregar 2 decimales
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logo", null=True, blank=True, verbose_name="foto"
    )

    def __str__(
        self,
    ) -> str:  # Aca llamo a str para que me devuelva el nombre del producto
        return self.name
