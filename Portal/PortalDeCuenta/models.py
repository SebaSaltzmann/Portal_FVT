from typing import Any
from django.db import models

class Usuarios(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Contraseña = models.CharField(max_length=255)
    Gmail = models.CharField(max_length=255)
# Create your models here.
