# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute1', models.IntegerField()),
                ('attribute2', models.CharField(max_length=20)),
            ],
        ),
    ]