# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_comment_legacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='insert_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
