# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsModule', '0001_initial'),
        ('userModule', '0004_remove_userinfo_usertelephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='goodsModule.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.CharField(serialize=False, primary_key=True, max_length=20)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_pay', models.BooleanField(default=False)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_address', models.CharField(max_length=150)),
                ('order_user', models.ForeignKey(to='userModule.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='orderModule.OrderInfo'),
        ),
    ]
