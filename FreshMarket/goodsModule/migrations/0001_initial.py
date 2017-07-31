# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsTitle', models.CharField(max_length=20)),
                ('goodsPic', models.ImageField(upload_to='goods')),
                ('goodsPrice', models.DecimalField(max_digits=6, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('goodsUnit', models.CharField(default='500g', max_length=20)),
                ('goodsClick', models.IntegerField()),
                ('goodsIntro', models.CharField(max_length=200)),
                ('goodsStorage', models.IntegerField()),
                ('goodsContent', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'tableGoodsInfo',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeTitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tableGoodsType',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='goodsType',
            field=models.ForeignKey(to='goodsModule.GoodsType'),
        ),
    ]
