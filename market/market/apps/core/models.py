# -*- coding: utf 8 -*-
from django.db import models
from django.conf import settings

from django_extensions.db.fields import RandomCharField

# Used to generate the random URLs for profiles, posts, and other.
class RandomSlugModel(models.Model):
    slug = RandomCharField(length=8, lowercase=True, unique=True)

    class Meta:
        abstract = True


class UserProfile(RandomSlugModel, models.Model):
    """
    This is an extension to the default User model, created on
    registration for each user. All relations to a User are through
    this model to maintain separation from the authentication backend.
    """
    ACCOUNT_TYPE_CHOICES = (
        ('0', ""),
        ('1', "Usuário"),
        ('2', "Loja"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    tipo = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='0')
    name = models.CharField('nome', max_length=200)
    phone_number1 = models.PhoneNumberField('telefone', max_length=50, default='')

    @property
    def is_seller(self):
        return self.tipo == self.ACCOUNT_TYPE_CHOICES[1][0]

    def __str__(self):
        return self.name
