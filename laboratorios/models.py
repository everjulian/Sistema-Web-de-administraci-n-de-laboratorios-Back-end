from django.db import models

class LaboratoriosModel(models.Model):
    nombre_laboratorio = models.CharField(max_length=255)

    class Meta:
        db_table = 'Laboratorios'
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"

    def __str__(self):
        return self.nombre_laboratorio
