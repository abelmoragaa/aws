
from django.db import models
from django.contrib.auth.models import User   

class Cita(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del cliente
    rut = models.CharField(max_length=12)  # RUT del cliente
    fecha = models.DateField()  # Fecha de la cita
    hora = models.TimeField()  # Hora de la cita
    motivo = models.TextField()  # Motivo o descripción de la cita

    def __str__(self):
        return f"Cita con {self.nombre} el {self.fecha} a las {self.hora}"
