# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0005_auto_20181204_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='like',
            new_name='praise',
        ),
    ]
