# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0002_auto_20150629_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsetting',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date Created'),
        ),
    ]
