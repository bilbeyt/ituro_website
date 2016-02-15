# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(choices=[(b'general_photos', 'General Photos'), (b'all_categories', 'All Categories'), (b'sponsorship', 'Sponsorship'), (b'news', 'News'), (b'line_follower', 'Line Follower'), (b'basketball', 'Basketball'), (b'micro_sumo', 'Micro Sumo'), (b'fire_fighter', 'Fire Fighter'), (b'stair_climbing', 'Stair Climbing'), (b'maze', 'Maze'), (b'color_selecting', 'Color Selecting'), (b'self_balancing', 'Self Balancing'), (b'scenario', 'Scenario'), (b'innovative', 'Innovative')], max_length=50),
        ),
    ]
