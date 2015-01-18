# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0009_auto_20150118_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='contact2',
            field=models.ForeignKey(related_name='venueContact', default=1, to='shows.contact'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
