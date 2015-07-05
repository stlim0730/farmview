# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appearance', models.CharField(max_length=20)),
                ('calculation', models.CharField(max_length=20)),
                ('constraint', models.CharField(max_length=20)),
                ('constraint_message', models.CharField(max_length=100)),
                ('default', models.CharField(max_length=20)),
                ('hint_english', models.CharField(max_length=600)),
                ('hint_espanol', models.CharField(max_length=600)),
                ('label_english', models.CharField(max_length=600)),
                ('label_espanol', models.CharField(max_length=600)),
                ('name', models.CharField(max_length=20)),
                ('relevant', models.CharField(max_length=20)),
                ('required', models.BooleanField()),
                ('q_type', models.CharField(max_length=20)),
            ],
        ),
    ]
