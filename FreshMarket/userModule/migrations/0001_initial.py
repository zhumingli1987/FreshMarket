# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('addressInfo', models.CharField(verbose_name='addressInfo', max_length=150)),
                ('addressId', models.IntegerField(verbose_name='addressId', max_length=6)),
            ],
            options={
                'db_table': 'addressTable',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'goodsTable',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(verbose_name='orderId', serialize=False, max_length=12, primary_key=True)),
                ('orderTime', models.DateTimeField(verbose_name='orderTime', auto_now_add=True)),
                ('payInfo', models.BooleanField(verbose_name='payInfo', default='false')),
                ('moneyCount', models.FloatField(verbose_name='moneyCount')),
                ('orderGoods', models.ManyToManyField(to='userModule.Goods')),
            ],
            options={
                'db_table': 'orderTable',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.IntegerField(auto_created=True, verbose_name='userId', max_length=10, primary_key=True, serialize=False)),
                ('userName', models.CharField(verbose_name='userName', max_length=20, null='false')),
                ('password', models.CharField(verbose_name='password', max_length=40, null='false')),
                ('email', models.CharField(verbose_name='email', max_length=40, null='false')),
                ('telephone', models.CharField(verbose_name='telephone', max_length=20)),
            ],
            options={
                'db_table': 'userTable',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='orderUser',
            field=models.ForeignKey(to='userModule.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='addressUser',
            field=models.ForeignKey(to='userModule.User'),
        ),
    ]
