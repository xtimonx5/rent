# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20170212_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]