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
            field=models.IntegerField(verbose_name='addressId', auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='mailId',
            field=models.IntegerField(verbose_name='mailId'),
        ),
    ]
