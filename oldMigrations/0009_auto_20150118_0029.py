# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0008_auto_20150118_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='contact',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
