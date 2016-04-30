# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(blank=False, null=False, max_length=255)
    texto = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    texto = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    usuario = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name="comentarios")

    def __unicode__(self):
        return str(self.pk)