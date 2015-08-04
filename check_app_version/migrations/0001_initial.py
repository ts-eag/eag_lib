# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_id', models.CharField(max_length=20)),
                ('app_version', models.CharField(max_length=10)),
                ('apk_file', models.FileField(upload_to=b'apk/')),
                ('apk_size', models.IntegerField()),
                ('download_cnt', models.BigIntegerField(default=0)),
                ('register_date', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
