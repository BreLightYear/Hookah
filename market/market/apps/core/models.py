# -*- coding: utf 8 -*-
from django.db import models
from django.conf import settings


from django_extensions.db.fields import RandomCharField

# Used to generate the random URLs for profiles, posts, and other.
class RandomSlugModel(models.Model):
    slug = RandomCharField(length=8, lowercase=True, unique=True)

    class Meta:
        abstract = True


class UserProfile(RandomSlugModel):
    """
    This is an extension to the default User model, created on
    registration for each user. All relations to a User are through
    this model to maintain separation from the authentication backend.
    """
    ACCOUNT_TYPE_CHOICES = [
        ('0', ""),
        ('1', "Usuário"),
        ('2', "Loja"),
    ]

    TYPE_SEX = [
        ('0', ""),
        ('1', "Masculino"),
        ('2', "Feminino"),
    ]

    DISTRICT = [
        ('0', "Escolha sua cidade"),
        ('1', "Diadema"),
        ('2', "São Bernardo do Campo"),
        ('3', "Santo André"),
        ('4', "São Caetano"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    tipo = models.CharField(max_length=1, choices= ACCOUNT_TYPE_CHOICES, blank=True, default=0)
    name = models.CharField('nome', max_length=200)
    sexo = models.CharField(max_length=1, choices=TYPE_SEX, blank=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    adress_number = models.CharField(max_length=16, blank=True, null=True)
    district = models.CharField(max_length=1, choices= DISTRICT, blank=True, default=0)
    created_in = models.DateField(auto_now_add=True, blank=True, null=True)
    
    @property
    def is_seller(self):
        return self.tipo == self.ACCOUNT_TYPE_CHOICES[1][0]

    def __str__(self):
        return self.name
