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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('goodsTitle', models.CharField(max_length=20)),
                ('goodsIntro', models.CharField(max_length=200)),
                ('goodsPic', models.ImageField(upload_to='goods')),
                ('goodsPrice', models.DecimalField(max_digits=6, decimal_places=2)),
                ('goodsUnit', models.CharField(default='500g', max_length=20)),
                ('goodsClick', models.IntegerField()),
                ('goodsStock', models.IntegerField()),
                ('goodsContent', tinymce.models.HTMLField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('typeTitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='goodsType',
            field=models.ForeignKey(to='goodsModule.GoodsType'),
        ),
    ]
