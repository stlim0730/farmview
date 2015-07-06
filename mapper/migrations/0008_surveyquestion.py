# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0007_auto_20150629_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('label_english', models.TextField()),
                ('label_espanol', models.TextField()),
                ('hint_english', models.TextField()),
                ('hint_espanol', models.TextField()),
                ('required', models.BooleanField()),
                ('constraint', models.CharField(max_length=30)),
                ('constraint_message', models.TextField()),
                ('relevant', models.TextField()),
                ('default', models.CharField(max_length=30)),
                ('appearance', models.CharField(max_length=30)),
                ('calculation', models.CharField(max_length=30)),
            ],
        ),
    ]
