# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-03 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0002_auto_20180102_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogsuploaded',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
