# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0011_auto_20170901_2055'),
        ('user', '0002_user_legacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following_list',
            field=models.ManyToManyField(blank=True, to='phone.Phone'),
        ),
    ]
