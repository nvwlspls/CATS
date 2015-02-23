# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0012_venue_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='homeState',
            field=models.CharField(default=b'None', max_length=50),
            preserve_default=True,
        ),
    ]
