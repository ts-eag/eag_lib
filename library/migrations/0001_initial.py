# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.conf import settings
import library.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('added_time', models.DateTimeField(default=django.utils.timezone.now, help_text=b'\xec\xa2\x8c\xec\x84\x9d\xec\x9d\x84 \xec\xb2\x98\xec\x9d\x8c \xeb\x93\xb1\xeb\xa1\x9d\xed\x95\x9c \xec\x8b\x9c\xea\xb0\x84')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, help_text=b'\xeb\xb3\xb4\xec\xa0\x95(30\xeb\xb6\x84 \xeb\x8b\xa8\xec\x9c\x84)\xec\x9d\xb4 \xec\x9d\xb4\xeb\xa3\xa8\xec\x96\xb4\xec\xa7\x84 \xec\x8b\xa4\xec\xa0\x9c \xeb\x8f\x84\xec\x84\x9c\xea\xb4\x80 \xec\x9d\xb4\xec\x9a\xa9 \xec\x8b\x9c\xec\x9e\x91 \xec\x8b\x9c\xea\xb0\x84')),
                ('end_time', models.DateTimeField(default=library.models.get_end_time)),
                ('is_now', models.BooleanField(default=True, help_text=b'\xed\x98\x84\xec\x9e\xac\xec\x8b\x9c\xea\xb0\x84\xeb\xb6\x80\xed\x84\xb0 \xeb\x8f\x84\xec\x84\x9c\xea\xb4\x80 \xec\x82\xac\xec\x9a\xa9')),
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=25, null=True, blank=True)),
                ('user', models.OneToOneField(related_name=b'profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
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
            field=models.ForeignKey(to='library.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extensiontime',
            name='user',
            field=models.ForeignKey(to='library.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='extensiontime',
            unique_together=set([('user', 'date')]),
        ),
    ]
