# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0010_auto_20171011_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 11, 13, 12, 23, 770436, tzinfo=utc)),
        ),
    ]