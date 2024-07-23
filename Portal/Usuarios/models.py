from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.BigIntegerField(auto_created=True, primary_key=True, null=False)
    Nombre = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Contraseña = models.CharField(max_length=255)