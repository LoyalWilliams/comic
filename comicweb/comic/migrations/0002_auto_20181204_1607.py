# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
