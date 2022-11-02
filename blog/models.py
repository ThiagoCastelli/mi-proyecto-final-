from email.policy import default
from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14, default='')
    construido_por = models.CharField(max_length=30, default='')
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')

    
