# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-10 07:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 7, 48, 56, 951919, tzinfo=utc)),
        ),
    ]