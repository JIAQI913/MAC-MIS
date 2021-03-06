# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-21 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0005_project_pro_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Fac_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Fac_position',
            field=models.CharField(choices=[('Director', 'Director'), ('Professor', 'Professor'), ('Associate Professor', 'Associate Professor'), ('Instructor', 'Instructor')], default='Instructor', max_length=2),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Fac_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='city',
            field=models.CharField(default='Windsor', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty',
            name='province',
            field=models.CharField(choices=[('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec'), ('BC', 'British Columbia'), ('NS', 'Nova Scotia'), ('SK', 'Saskatchewan'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NT', 'Northwest Territories'), ('YT', 'Yukon'), ('NU', 'Nunabut')], default='ON', max_length=2),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Staff_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Staff_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='city',
            field=models.CharField(default='Windsor', max_length=20),
        ),
        migrations.AddField(
            model_name='staff',
            name='province',
            field=models.CharField(choices=[('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec'), ('BC', 'British Columbia'), ('NS', 'Nova Scotia'), ('SK', 'Saskatchewan'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NT', 'Northwest Territories'), ('YT', 'Yukon'), ('NU', 'Nunabut')], default='ON', max_length=2),
        ),
    ]
