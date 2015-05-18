# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0005_auto_20150518_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birthday',
            new_name='birthdate',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 22, 47, 44, 937554)),
        ),
    ]
