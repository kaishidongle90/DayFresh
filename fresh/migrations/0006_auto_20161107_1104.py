# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0005_auto_20161107_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='justsaw',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelTable(
            name='justsaw',
            table='justsaw',
        ),
    ]
