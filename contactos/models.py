from django.db import models


# Create your models here.

class Contacto_Model(models.Model):
    nombre = models.CharField(max_length=50, unique=True, blank = True, null = False)
    apellido = models.CharField(max_length=50, blank = True, null = False)
    email = models.EmailField(blank = True, null = False)
    telefono_1 = models.CharField(max_length=10, null = True, blank = True, unique = True)
    telefono_2 = models.CharField(max_length=10, null = True, blank = True, unique = True)
    compañia = models.CharField(max_length=50, null = False, blank = True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
