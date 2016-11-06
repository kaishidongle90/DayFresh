# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0002_auto_20161102_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gpicb',
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gpicl',
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(default=datetime.datetime(2016, 11, 4, 3, 56, 9, 305333, tzinfo=utc), upload_to=b'fresh/images/goods/'),
            preserve_default=False,
        ),
    ]
