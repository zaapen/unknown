# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-23 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='travel_end',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='travel_start',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
    ]
