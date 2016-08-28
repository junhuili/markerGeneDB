# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('rank', models.CharField(max_length=15, choices=[(1, 'Kingdom'), (2, 'Phylum'), (3, 'Class'), (4, 'Order'), (5, 'Family'), (5, 'Genus'), (5, 'Species')])),
            ],
        ),
        migrations.CreateModel(
            name='Typestrain',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
                ('atcc_num', models.CharField(max_length=15, verbose_name='ATCC Number')),
                ('dsm_num', models.CharField(max_length=15, verbose_name='DSM Number')),
                ('seq_id', models.CharField(max_length=100, verbose_name='Sequence ID Number')),
                ('category_abbrv', models.CharField(max_length=100, verbose_name='Category Abbreviation')),
            ],
        ),
        migrations.CreateModel(
            name='Valid',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
                ('rank', models.CharField(max_length=20, verbose_name='ATCC Number')),
                ('category_abbrv', models.CharField(max_length=100, verbose_name='Category Abbreviation')),
                ('seq_id', models.CharField(max_length=100, verbose_name='Sequence ID Number')),
            ],
        ),
    ]
