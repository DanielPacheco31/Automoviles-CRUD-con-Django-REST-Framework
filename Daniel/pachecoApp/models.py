from django.db import models

class Automovil(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.IntegerField()
    diseño = models.CharField(max_length=100)
    cilindraje = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.marca} ({self.modelo})"
    
    class Meta:
        verbose_name = "Automóvil"
        verbose_name_plural = "Automóviles"
