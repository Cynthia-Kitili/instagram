# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-19 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Type Bio:', max_length=300),
        ),
    ]
