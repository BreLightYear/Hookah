# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-20 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190817_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number1',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
