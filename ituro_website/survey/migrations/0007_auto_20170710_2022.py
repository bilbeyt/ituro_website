# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-10 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20170710_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textareaquestion',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
