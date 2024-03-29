# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-07 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import djgeojson.fields
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('slug', django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=8, lowercase=True, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('unit', models.CharField(choices=[(b'pound', b'POUND'), (b'gallon', b'GALLON'), (b'each', b'EACH')], default=b'each', max_length=80)),
                ('location', djgeojson.fields.PointField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='board.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tagulous_Post_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='tagulous_post_tags',
            unique_together=set([('slug',)]),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=True, help_text='Enter a comma-separated tag string', max_count=10, space_delimiter=False, to='board.Tagulous_Post_tags'),
        ),
    ]
