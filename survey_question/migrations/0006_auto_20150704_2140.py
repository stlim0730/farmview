# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_question', '0005_auto_20150704_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='appearance',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='calculation',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='constraint',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='default',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='relevant',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='type',
            field=models.CharField(max_length=30),
        ),
    ]
