from django.db import models

class MarcasModel(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'Marcas'
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre
