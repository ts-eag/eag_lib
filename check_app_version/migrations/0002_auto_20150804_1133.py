# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check_app_version', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='apk_size',
            field=models.IntegerField(default=0),
        ),
    ]
