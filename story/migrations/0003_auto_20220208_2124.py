# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-08 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20220208_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerita',
            name='author',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]
