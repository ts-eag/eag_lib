# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import library.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtensionTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('frequency', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(default=library.models.get_end_time)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'\xeb\xb0\xa9\xec\x9d\x98 \xec\x9d\xb4\xeb\xa6\x84. \xeb\x82\xa8\xec\x9e\x90\xeb\xb0\xa9, \xec\x97\xac\xec\x9e\x90\xeb\xb0\xa9 \xea\xb0\x99\xec\x9d\xb4 \xeb\xb0\xa9\xec\x9d\x84 \xea\xb5\xac\xeb\xb6\x84\xed\x95\x98\xeb\x8a\x94\xeb\x8d\xb0 \xec\x82\xac\xec\x9a\xa9\xed\x95\x9c\xeb\x8b\xa4.', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat_num', models.PositiveIntegerField(unique=True)),
                ('room', models.ForeignKey(to='library.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(help_text=b'\xec\xa2\x8c\xec\x84\x9d \xec\x98\x88\xec\x95\xbd\xec\x9d\xb4 \xea\xb0\x80\xeb\x8a\xa5\xed\x95\x9c\xec\xa7\x80? Pass, Available', max_length=50)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(help_text=b'\xed\x98\x84\xec\x9e\xac \xec\xa2\x8c\xec\x84\x9d\xec\x9d\x98 \xed\x83\x80\xec\x9e\x85. \xec\xb9\xb8\xeb\xa7\x89\xec\x9d\xb4 \xec\x97\xac\xeb\xb6\x80, \xeb\x98\x90?', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seat',
            name='status',
            field=models.ForeignKey(to='library.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seat',
            name='type',
            field=models.ForeignKey(to='library.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat',
            field=models.ForeignKey(to='library.Seat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(to='library.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extensiontime',
            name='user',
            field=models.ForeignKey(to='library.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='extensiontime',
            unique_together=set([('user', 'date')]),
        ),
    ]
