# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_supervisor_initials'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thesis',
            old_name='grade_date',
            new_name='examination_date',
        ),
    ]