# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0005_auto_20150629_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsetting',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date created'),
        ),
    ]
