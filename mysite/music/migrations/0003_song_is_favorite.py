# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_song_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
