# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0013_band_homestate'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='zipCode',
            field=models.CharField(default=b'00000', max_length=9),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='contact2',
            field=models.ForeignKey(related_name='venueContact', default=b'email@email.com', to='shows.contact', null=True),
            preserve_default=True,
        ),
    ]
