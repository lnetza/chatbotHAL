"""
Definition of models.
"""

from django.db import models

class Encuestas(models.Model):
    id_chat = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    pregunta = models.CharField(max_length=450)
    respuesta = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % ( self.id_chat)

