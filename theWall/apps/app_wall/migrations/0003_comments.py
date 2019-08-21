# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-20 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
        ('app_wall', '0002_auto_20190820_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_wall.Messages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_login.Users')),
            ],
        ),
    ]
