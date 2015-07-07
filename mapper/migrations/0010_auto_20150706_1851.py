# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0009_surveyquestion_queryable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='queryable',
            field=models.BooleanField(default=False),
        ),
    ]
