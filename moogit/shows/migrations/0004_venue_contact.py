# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='contact',
            field=models.ForeignKey(related_name='venueContact', default=1, to='shows.contact'),
            preserve_default=False,
        ),
    ]
