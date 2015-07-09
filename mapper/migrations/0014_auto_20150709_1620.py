# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0013_auto_20150709_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveychoice',
            name='question',
            field=models.ForeignKey(to='mapper.SurveyQuestion', null=True),
        ),
    ]
