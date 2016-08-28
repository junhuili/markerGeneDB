# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatus',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
                ('seq_id', models.IntegerField(verbose_name='Sequence ID Number')),
            ],
        ),
        migrations.CreateModel(
            name='Invalid',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
                ('reference_url', models.URLField(verbose_name="(blank=True, default='')")),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
                ('authors', models.CharField(max_length=100, verbose_name='Author List')),
                ('journal', models.CharField(max_length=100, verbose_name='Journal Title')),
                ('publication_date', models.CharField(max_length=100, verbose_name='Journal Publication Date')),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
                ('nuc_sequence', models.TextField(verbose_name='Nucleotide Sequence')),
                ('seq_id', models.IntegerField(verbose_name='Sequence ID Number')),
            ],
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('taxon', models.OneToOneField(primary_key=True, serialize=False, to='browser.Taxon')),
            ],
        ),
        migrations.RemoveField(
            model_name='valid',
            name='rank',
        ),
        migrations.AddField(
            model_name='taxon',
            name='last_update',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='rank',
            field=models.SmallIntegerField(choices=[(1, 'Kingdom'), (2, 'Phylum'), (3, 'Class'), (4, 'Order'), (5, 'Family'), (6, 'Genus'), (7, 'Species')]),
        ),
        migrations.AlterField(
            model_name='typestrain',
            name='seq_id',
            field=models.IntegerField(verbose_name='Sequence ID Number'),
        ),
        migrations.AlterField(
            model_name='valid',
            name='seq_id',
            field=models.IntegerField(verbose_name='Sequence ID Number'),
        ),
        migrations.AddField(
            model_name='synonym',
            name='valid_name',
            field=models.ForeignKey(to='browser.Valid'),
        ),
    ]
