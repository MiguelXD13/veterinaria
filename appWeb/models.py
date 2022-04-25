from django.db import models

# Create your models here.

class Consulta(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=9)
    email=models.EmailField(max_length=60)
    mensaje=models.CharField(max_length=200)