# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_question', '0003_auto_20150704_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyquestion',
            old_name='q_type',
            new_name='type',
        ),
    ]
