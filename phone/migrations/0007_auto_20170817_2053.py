# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0006_auto_20170817_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonerating',
            name='value',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Celt'), (-1, 'Necelt')], null=True),
        ),
    ]
