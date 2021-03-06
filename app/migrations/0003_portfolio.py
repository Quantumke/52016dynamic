# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-30 14:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('project_link', models.CharField(max_length=100)),
                ('project_image1', models.ImageField(upload_to='images', verbose_name='image')),
                ('project_image2', models.ImageField(blank=True, upload_to='images', verbose_name='image2')),
                ('project_image3', models.ImageField(blank=True, upload_to='images', verbose_name='image3')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
