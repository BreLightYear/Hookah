# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-14 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[(b'0', b'Escolha seu tipo de cadastro'), (b'1', b'Usu\xc3\xa1rio'), (b'2', b'Loja')], default=b'0', max_length=1),
        ),
    ]
