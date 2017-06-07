# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='goodsinfo',
            table='tableGoodsInfo',
        ),
        migrations.AlterModelTable(
            name='goodstype',
            table='tableGoodsType',
        ),
    ]
