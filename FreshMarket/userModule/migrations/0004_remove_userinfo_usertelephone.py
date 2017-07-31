# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userModule', '0003_auto_20170605_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='userTelephone',
        ),
    ]
