# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='conEmail',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='conFirstName',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='conLastName',
        ),
    ]
