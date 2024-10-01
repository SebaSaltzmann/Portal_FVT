from django.db import models

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Passworld = models.CharField(max_length=255)
    Gmail = models.CharField(max_length=255)

    def __str__(self):
        return self.id

# Create your models here.
