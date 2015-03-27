# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_auto_20150122_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='genre',
            fields=[
                ('genreID', models.AutoField(serialize=False, primary_key=True)),
                ('genreName', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subGenre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subGenreName', models.CharField(max_length=100)),
                ('fk_GenreID', models.ForeignKey(related_name='subGenre_Genre', to='shows.genre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
