# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0002_auto_20150518_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 20, 57, 7, 977189)),
        ),
    ]
