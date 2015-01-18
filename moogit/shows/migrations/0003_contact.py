# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20150118_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=1, max_length=100)),
                ('firstName', models.CharField(default=b'first name', max_length=100)),
                ('lastName', models.CharField(default=b'last name', max_length=100)),
                ('nickname', models.CharField(default=b'nickname', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
