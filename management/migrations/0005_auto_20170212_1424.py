# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20170212_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rent',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
