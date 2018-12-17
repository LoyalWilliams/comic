# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('intr', models.CharField(max_length=300)),
                ('cover', models.CharField(max_length=100)),
                ('chapter_url', models.CharField(max_length=100)),
                ('comic_type', models.CharField(max_length=20)),
                ('comic_type2', models.CharField(max_length=20)),
                ('collection', models.IntegerField(default=0)),
                ('recommend', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('roast', models.IntegerField(default=0)),
                ('last_update_chapter', models.CharField(max_length=50)),
                ('last_update_time', models.DateTimeField()),
                ('status', models.SmallIntegerField(default=0)),
                ('add_time', models.DateTimeField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'comic',
            },
        ),
    ]
