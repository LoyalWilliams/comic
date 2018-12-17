# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0003_auto_20181204_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='like',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comic',
            name='roast',
            field=models.BigIntegerField(default=0),
        ),
    ]
