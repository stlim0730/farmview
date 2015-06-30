# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0004_auto_20150629_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsetting',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date created'),
        ),
    ]
