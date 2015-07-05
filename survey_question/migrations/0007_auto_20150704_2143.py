# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_question', '0006_auto_20150704_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='relevant',
            field=models.TextField(),
        ),
    ]
