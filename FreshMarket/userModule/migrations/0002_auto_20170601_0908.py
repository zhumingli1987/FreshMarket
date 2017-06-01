# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressId',
            field=models.IntegerField(verbose_name='addressId'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.IntegerField(auto_created=True, verbose_name='userId', primary_key=True, serialize=False),
        ),
    ]
