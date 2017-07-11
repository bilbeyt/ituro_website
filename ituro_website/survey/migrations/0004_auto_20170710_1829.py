# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-10 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20170710_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAreaQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=250, null=True)),
                ('answer', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey')),
            ],
        ),
        migrations.AlterField(
            model_name='textquestion',
            name='answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
