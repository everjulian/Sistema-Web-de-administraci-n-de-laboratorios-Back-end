from django.db import models
from laboratorios.models import LaboratoriosModel
from marcas.models import MarcasModel

class ActivosModel(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('EN_USO', 'En uso'),
        ('EN_REPARACION', 'En reparacion'),
    ]

    laboratorio = models.ForeignKey(LaboratoriosModel, related_name='activos', on_delete=models.CASCADE)
    codigo_activo = models.CharField(max_length=12)
    nombre_activo = models.CharField(max_length=25)
    marca = models.ForeignKey(MarcasModel, related_name='activos', on_delete=models.CASCADE)
    estado = models.CharField(max_length=16, choices=ESTADO_CHOICES, default='DISPONIBLE')
    descripcion = models.TextField(blank=True)

    class Meta:
        db_table = 'Activos'
        verbose_name = "Activo"
        verbose_name_plural = "Activos"

    def __str__(self):
        return f"{self.nombre_activo} ({self.codigo_activo})"
