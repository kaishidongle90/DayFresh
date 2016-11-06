# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0003_auto_20161104_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetialInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dnum', models.IntegerField(default=0)),
                ('dtotal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('dgoods', models.ForeignKey(to='fresh.GoodsInfo')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'orderDetialInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('odate', models.DateTimeField()),
                ('ototalprice', models.DecimalField(max_digits=6, decimal_places=2)),
                ('ispay', models.BooleanField(default=False)),
                ('ouser', models.ForeignKey(to='fresh.UserInfo')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'orderInfo',
            },
        ),
        migrations.RemoveField(
            model_name='cartinfo',
            name='isDelete',
        ),
        migrations.AlterModelTable(
            name='cartinfo',
            table='cartInfo',
        ),
        migrations.AddField(
            model_name='orderdetialinfo',
            name='dorder',
            field=models.ForeignKey(to='fresh.OrderInfo'),
        ),
    ]
