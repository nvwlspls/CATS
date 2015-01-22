# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20150120_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='orders',
            field=models.ManyToManyField(related_name='orders', null=True, to='shows.showOrder'),
            preserve_default=True,
        ),
    ]
