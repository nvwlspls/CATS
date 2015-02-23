# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0010_auto_20150118_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='subGenre',
            field=models.CharField(default='apples', max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=b'email@email.com', max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='contact2',
            field=models.ForeignKey(related_name='venueContact', default=b'email@email.com', to='shows.contact'),
            preserve_default=True,
        ),
    ]
