# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20150122_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='age',
            field=models.CharField(max_length=3, null=True),
            preserve_default=True,
        ),
    ]
