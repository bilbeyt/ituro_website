# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-11 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20170711_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='is_chosen',
        ),
    ]
