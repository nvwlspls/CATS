# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('bandID', models.AutoField(serialize=False, primary_key=True)),
                ('bandName', models.CharField(default=b'Band Name', max_length=200)),
                ('homeTown', models.CharField(default=b'Home Town', max_length=100)),
                ('homeState', models.CharField(default=b'None', max_length=50)),
                ('genre', models.CharField(max_length=75)),
                ('subGenre', models.CharField(max_length=75)),
                ('bandDateAdded', models.DateTimeField(auto_now_add=True)),
                ('bandDateMod', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('email', models.EmailField(default=b'email@email.com', max_length=100, serialize=False, primary_key=True)),
                ('firstName', models.CharField(default=b'first name', max_length=100)),
                ('lastName', models.CharField(default=b'last name', max_length=100)),
                ('nickname', models.CharField(default=b'nickname', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('show2ID', models.AutoField(serialize=False, primary_key=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('DateTimeAdded', models.DateTimeField(auto_now_add=True)),
                ('DateTimeMod', models.DateTimeField(auto_now=True)),
                ('bandExtraTesxt', models.TextField()),
                ('age', models.IntegerField()),
                ('cost', models.DecimalField(max_digits=5, decimal_places=2)),
                ('bands', models.ManyToManyField(related_name='bands', to='shows.Band')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='showOrder',
            fields=[
                ('showOrderID', models.AutoField(serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
                ('bandID', models.ForeignKey(related_name='bandIDOrder', to='shows.Band')),
                ('showID', models.ForeignKey(related_name='showIDOrder', to='shows.show')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venueID', models.AutoField(serialize=False, primary_key=True)),
                ('venueName', models.CharField(default=b'Venue Name', max_length=75)),
                ('description', models.TextField()),
                ('area', models.CharField(max_length=20, choices=[(b'NC', b'North County'), (b'EC', b'East County'), (b'CC', b'Central'), (b'SB', b'South Boy')])),
                ('neighborhood', models.CharField(default=b'Neighborhood', max_length=75)),
                ('venueDateAdded', models.DateTimeField(auto_now_add=True)),
                ('venueLastMod', models.DateTimeField(auto_now=True)),
                ('streetAddress', models.CharField(default=b'Street Address', max_length=150)),
                ('city', models.CharField(default=b'City', max_length=150)),
                ('state', models.CharField(default=b'None', max_length=50)),
                ('zipCode', models.CharField(default=b'00000', max_length=9, null=True)),
                ('contact2', models.ForeignKey(related_name='contact2', to='shows.contact', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='show',
            name='orders',
            field=models.ManyToManyField(related_name='orders', to='shows.showOrder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='show',
            name='showVenueID',
            field=models.ForeignKey(to='shows.Venue'),
            preserve_default=True,
        ),
    ]
