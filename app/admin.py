"""
Se registra el modelo Encuestas para poder accederlo desde el administrador de Django
"""
from django.contrib import admin
from .models import Encuestas

admin.site.register(Encuestas)