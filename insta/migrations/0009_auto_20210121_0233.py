# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-20 23:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_auto_20210121_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['profile']},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ['user_to', 'user_from']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_name']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user']},
        ),
    ]
