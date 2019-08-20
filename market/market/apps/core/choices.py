# -*- coding: utf 8 -*-
from django.db import models
from django.conf import settings

from django_extensions.db.fields import RandomCharField

def ACCOUNT_TYPE_CHOICES:
    ACCOUNT_TYPE_CHOICES = (
        ('0', ""),
        ('1', "Usuário"),
        ('2', "Loja"),
    )

ACCOUNT_TYPE_CHOICES = (
        ('0', ""),
        ('1', "Usuário"),
        ('2', "Loja"),
    )

TYPE_SEX = (
        ('0', ""),
        ('1', "Masculino"),
        ('2', "Feminino"),
    )