# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vizjson_url', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('optional_note', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyChoice',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('list_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('label_english', models.TextField(blank=True)),
                ('label_espanol', models.TextField(blank=True)),
                ('image', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('label_english', models.TextField(blank=True)),
                ('label_espanol', models.TextField(blank=True)),
                ('hint_english', models.TextField(blank=True)),
                ('hint_espanol', models.TextField(blank=True)),
                ('required', models.BooleanField()),
                ('constraint', models.CharField(max_length=30, blank=True)),
                ('constraint_message', models.TextField(blank=True)),
                ('relevant', models.TextField(blank=True)),
                ('default', models.CharField(max_length=30, blank=True)),
                ('appearance', models.CharField(max_length=30, blank=True)),
                ('calculation', models.CharField(max_length=30, blank=True)),
                ('queryable', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='surveychoice',
            name='question',
            field=models.ForeignKey(to='map.SurveyQuestion', null=True),
        ),
    ]
