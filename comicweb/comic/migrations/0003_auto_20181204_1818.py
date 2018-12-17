# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0002_auto_20181204_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='chapter_url',
            new_name='comic_url',
        ),
    ]
