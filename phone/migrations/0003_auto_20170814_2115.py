# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_auto_20170814_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='cat_1',
            field=models.CharField(blank=True, editable=False, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='cat_2',
            field=models.CharField(blank=True, editable=False, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='cat_3',
            field=models.CharField(blank=True, editable=False, max_length=6, null=True),
        ),
    ]
