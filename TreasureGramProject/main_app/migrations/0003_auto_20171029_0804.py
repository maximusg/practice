# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20171029_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
