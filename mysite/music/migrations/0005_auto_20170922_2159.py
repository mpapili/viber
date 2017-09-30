# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170922_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(default='none', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(default='none', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(default='none', max_length=100, null=True),
        ),
    ]
