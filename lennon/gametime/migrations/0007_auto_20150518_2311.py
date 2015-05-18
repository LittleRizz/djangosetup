# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0006_auto_20150518_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 23, 11, 13, 454713)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_hobby',
            field=models.ForeignKey(to='gametime.Hobby'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hair_color',
            field=models.CharField(blank=True, max_length=128, choices=[(b'BLACK', b'Black'), (b'BROWN', b'Brown'), (b'RED', b'Red'), (b'BLONDE', b'Blonde'), (b'SALTNPEPPER', b'Salt N Peppa'), (b'GREEN', b'Green'), (b'BALD', b'Fucking Bald')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
