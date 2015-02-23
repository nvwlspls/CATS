# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_remove_venue_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact',
        ),
    ]
