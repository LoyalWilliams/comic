# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0004_auto_20181204_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='intr',
            field=models.CharField(max_length=500),
        ),
    ]
