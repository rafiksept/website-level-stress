# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-08 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20220208_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerita',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
