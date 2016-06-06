# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=200, unique=True)),
                ('balance', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('reg_date', models.DateTimeField(auto_now_add=True, unique=True)),
            ],
        ),
    ]
