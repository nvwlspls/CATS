# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0014_auto_20150119_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='zipCode',
            field=models.CharField(default=b'00000', max_length=9, null=True),
            preserve_default=True,
        ),
    ]
