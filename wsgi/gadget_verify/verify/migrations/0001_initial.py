# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('pmid', models.IntegerField(serialize=False, primary_key=True)),
                ('link', models.URLField()),
                ('author', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relevant', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('entrez', models.IntegerField()),
                ('true_relevance', models.BooleanField(default=True)),
                ('symbol', models.CharField(max_length=200)),
                ('synonyms', models.TextField()),
                ('abstracts', models.ManyToManyField(to='verify.Abstract')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('genes', models.ManyToManyField(to='verify.Gene', through='verify.Choice')),
                ('query', models.ForeignKey(to='verify.Query')),
            ],
        ),
        migrations.AddField(
            model_name='gene',
            name='query',
            field=models.ForeignKey(to='verify.Query'),
        ),
        migrations.AddField(
            model_name='choice',
            name='gene',
            field=models.ForeignKey(to='verify.Gene'),
        ),
        migrations.AddField(
            model_name='choice',
            name='surveyor',
            field=models.ForeignKey(to='verify.Surveyor'),
        ),
    ]
