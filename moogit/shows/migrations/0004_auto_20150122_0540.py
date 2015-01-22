# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20150121_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='bands',
            field=models.ManyToManyField(related_name='bands', null=True, to='shows.Band'),
            preserve_default=True,
        ),
    ]
