# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
