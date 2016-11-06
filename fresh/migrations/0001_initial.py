# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cbuy_date', models.DateTimeField()),
                ('cnum', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'cartinfo',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('gsubname', models.CharField(max_length=70)),
                ('gdesc', tinymce.models.HTMLField()),
                ('geval', tinymce.models.HTMLField(null=True, blank=True)),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gunit', models.CharField(max_length=20)),
                ('gpicl', models.ImageField(upload_to=b'fresh/images/goodsl/')),
                ('gpicb', models.ImageField(upload_to=b'fresh/images/goodsb/')),
                ('gpubdate', models.DateTimeField()),
                ('gsales', models.IntegerField(default=0)),
                ('gcounts', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'goodsinfo',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'goodstype',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=30)),
                ('uphoneNum', models.BigIntegerField(default=0, null=True, blank=True)),
                ('uaddress', models.CharField(max_length=50, null=True, blank=True)),
                ('uemail', models.EmailField(max_length=254)),
                ('upostcode', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='fresh.GoodsType'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='cgoods',
            field=models.ForeignKey(to='fresh.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='cuser',
            field=models.ForeignKey(to='fresh.UserInfo'),
        ),
    ]
