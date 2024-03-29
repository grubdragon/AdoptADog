# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-02 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Dog',
                'verbose_name_plural': 'Dogs',
            },
        ),
        migrations.CreateModel(
            name='DogsUploaded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('image_link', models.URLField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt.Dog')),
            ],
            options={
                'verbose_name': 'DogsUploaded',
                'verbose_name_plural': 'DogsUploadeds',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('rating', models.FloatField()),
                ('dogs_adopted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs_adopted', to='adopt.Dog')),
                ('dogs_putup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs_putup', to='adopt.Dog')),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
        migrations.AddField(
            model_name='dogsuploaded',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt.UserProfile'),
        ),
    ]
