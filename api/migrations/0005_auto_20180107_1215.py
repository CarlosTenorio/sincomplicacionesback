# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171225_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='shipping_costs',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitud'),
        ),
    ]
