# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 11:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20170419_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='grade',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
