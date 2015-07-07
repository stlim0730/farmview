# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0011_auto_20150706_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='label_english',
            field=models.TextField(blank=True),
        ),
    ]
