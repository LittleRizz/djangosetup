# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0004_auto_20150518_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 21, 0, 7, 902779)),
        ),
    ]
