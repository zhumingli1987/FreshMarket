# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userModule', '0002_auto_20170605_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='addressUser',
            new_name='addToUser',
        ),
        migrations.RemoveField(
            model_name='address',
            name='addressTelephone',
        ),
        migrations.AddField(
            model_name='address',
            name='receiveTel',
            field=models.CharField(max_length=20, null='false', verbose_name='receiveTel'),
        ),
    ]
