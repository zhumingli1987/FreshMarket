# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userModule', '0004_remove_userinfo_usertelephone'),
        ('goodsModule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='goodsModule.GoodsInfo')),
                ('user', models.ForeignKey(to='userModule.UserInfo')),
            ],
        ),
    ]
