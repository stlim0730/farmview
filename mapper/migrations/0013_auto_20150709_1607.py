# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0012_auto_20150706_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyChoice',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('list_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('label_english', models.TextField(blank=True)),
                ('label_espanol', models.TextField(blank=True)),
                ('image', models.CharField(max_length=30, blank=True)),
                ('question', models.ForeignKey(to='mapper.SurveyQuestion')),
            ],
        ),
        migrations.RenameModel(
            old_name='AdminSetting',
            new_name='Config',
        ),
    ]
