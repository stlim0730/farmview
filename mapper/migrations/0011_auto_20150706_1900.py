# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0010_auto_20150706_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='appearance',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='calculation',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='constraint',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='constraint_message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='default',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='hint_english',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='hint_espanol',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='label_espanol',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='relevant',
            field=models.TextField(blank=True),
        ),
    ]
