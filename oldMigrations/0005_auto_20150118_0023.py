# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_venue_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='contact',
            field=models.ForeignKey(related_name='venueContact', default=1, to='shows.contact'),
            preserve_default=True,
        ),
    ]
