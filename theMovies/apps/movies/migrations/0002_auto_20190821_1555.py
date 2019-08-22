# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-21 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='movie',
        ),
        migrations.AddField(
            model_name='movies',
            name='actors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.Actors'),
            preserve_default=False,
        ),
    ]
