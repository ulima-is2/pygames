# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=20)


class Post(models.Model):
    TECNOLOGIA = 'TE'
    ACTUALIDAD = 'AC'
    POLITICA = 'PO'
    ENTRETENIMIENTO = 'EN'

    CATEGORIAS_CHOICES = (
        (TECNOLOGIA, 'Tecnología'),
        (ACTUALIDAD, 'Actualidad'),
        (POLITICA, 'Política'),
        (ENTRETENIMIENTO, 'Entretenimiento'),
    )

    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=500)
    fecha_pub = models.DateTimeField('date published')
    usuario_pub = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS_CHOICES,
        default=ACTUALIDAD,
    )
