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
                ('addressId', models.IntegerField(serialize=False, primary_key=True, verbose_name='addressId')),
                ('addressInfo', models.CharField(null='false', verbose_name='addressInfo', max_length=150)),
                ('receiveName', models.CharField(null='false', verbose_name='receiveName', max_length='10')),
                ('mailId', models.IntegerField(verbose_name='mailId', max_length=10)),
                ('addressTelephone', models.CharField(null='false', verbose_name='addressTelephone', max_length=20)),
            ],
            options={
                'db_table': 'tableAddress',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userID', models.IntegerField(serialize=False, auto_created=True, primary_key=True, verbose_name='userId')),
                ('userName', models.CharField(null='false', verbose_name='userName', max_length=20)),
                ('password', models.CharField(null='false', verbose_name='password', max_length=40)),
                ('email', models.CharField(null='false', verbose_name='email', max_length=40)),
                ('userTelephone', models.CharField(verbose_name='userTelephone', max_length=20)),
                ('isDelete', models.BooleanField(default='false')),
            ],
            options={
                'db_table': 'tableUser',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='addressUser',
            field=models.ForeignKey(to='userModule.UserInfo'),
        ),
    ]
