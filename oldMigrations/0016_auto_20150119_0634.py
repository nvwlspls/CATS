# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0015_auto_20150119_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='contact2',
            field=models.ForeignKey(related_name='contact2', default=b'email@email.com', to='shows.contact', null=True),
            preserve_default=True,
        ),
    ]
