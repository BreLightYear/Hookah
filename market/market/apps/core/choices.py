# -*- coding: utf 8 -*-
from django.db import models
from django.conf import settings

from django_extensions.db.fields import RandomCharField

ACCOUNT_TYPE_CHOICES = (
        ('0', ""),
        ('1', "Usuário"),
        ('2', "Loja")
)

TYPE_SEX = (
        ('0', ""),
        ('1', "Masculino"),
        ('2', "Feminino")
)

DISTRICT = (
        ('0', "Escolha sua cidade"),
        ('1', "Diadema"),
        ('2', "São Bernardo do Campo"),
        ('3', "Santo André"),
        ('4', "São Caetano")
)