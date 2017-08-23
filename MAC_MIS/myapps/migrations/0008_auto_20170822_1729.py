# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0007_auto_20170822_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('I', 'International'), ('C', 'Citizen')], default='I', max_length=2),
        ),
    ]
