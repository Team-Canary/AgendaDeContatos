# -*- encoding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

class ItemAgenda(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    telefone1 = models.CharField(max_length=14)
    telefone2 = models.CharField(max_length=14, blank=True)
    endereco = models.CharField(max_length=100)
    redeSocial = models.CharField(max_length=100, blank=True)
    usuario = models.ForeignKey(User)
        
