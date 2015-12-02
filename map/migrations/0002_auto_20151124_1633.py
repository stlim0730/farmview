# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryField',
            fields=[
                ('query_field_id', models.AutoField(serialize=False, primary_key=True)),
                ('query_field_type', models.CharField(max_length=20, choices=[(b'text', b'Text'), (b'select_one', b'Select One'), (b'range', b'Range of Values')])),
                ('query_field_name', models.CharField(max_length=60)),
                ('query_field_label_eng', models.CharField(max_length=30)),
                ('query_field_label_esp', models.CharField(max_length=30, blank=True)),
                ('data_sources', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
                ('query_choices_vals', models.TextField(blank=True)),
                ('query_choices_labels_eng', models.TextField(blank=True)),
                ('query_choices_labels_esp', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='surveychoice',
            name='question',
        ),
        migrations.DeleteModel(
            name='SurveyChoice',
        ),
        migrations.DeleteModel(
            name='SurveyQuestion',
        ),
    ]
