# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_question', '0002_auto_20150704_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
