# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0008_surveyquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='queryable',
            field=models.BooleanField(default=True),
        ),
    ]
