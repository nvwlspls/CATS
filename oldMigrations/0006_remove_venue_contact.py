# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_auto_20150118_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='contact',
        ),
    ]
