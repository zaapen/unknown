# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-23 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0004_auto_20171123_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='travel_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='travel_start',
            field=models.DateField(),
        ),
    ]
