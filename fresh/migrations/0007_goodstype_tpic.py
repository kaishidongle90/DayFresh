# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0006_auto_20161107_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodstype',
            name='tpic',
            field=models.ImageField(default=datetime.datetime(2016, 11, 8, 1, 49, 13, 895482, tzinfo=utc), upload_to=b'fresh/images/goods/'),
            preserve_default=False,
        ),
    ]
