# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0004_auto_20161105_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='JustSaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jgoodsid', models.CharField(max_length=20000)),
            ],
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gname',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
