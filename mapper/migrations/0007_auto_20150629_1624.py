# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0006_auto_20150629_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsetting',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
