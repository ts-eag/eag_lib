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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('end_time', models.DateTimeField(default=library.models.get_end_time)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('seat_num', models.PositiveIntegerField(unique=True)),
                ('room_id', models.ForeignKey(to='library.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seat',
            name='status_id',
            field=models.ForeignKey(to='library.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seat',
            name='type_id',
            field=models.ForeignKey(to='library.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat_id',
            field=models.ForeignKey(to='library.Seat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_id',
            field=models.ForeignKey(to='library.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extensiontime',
            name='user_id',
            field=models.ForeignKey(to='library.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='extensiontime',
            unique_together=set([('user_id', 'date')]),
        ),
    ]
