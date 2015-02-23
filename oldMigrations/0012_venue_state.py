# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0011_auto_20150119_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='state',
            field=models.CharField(default=b'None', max_length=50),
            preserve_default=True,
        ),
    ]
