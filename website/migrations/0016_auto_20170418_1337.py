# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20170418_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='pdf_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]