# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_question', '0004_auto_20150704_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='constraint_message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='hint_english',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='hint_espanol',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='label_english',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='label_espanol',
            field=models.TextField(),
        ),
    ]
