# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20150825_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='notice_type',
            field=models.CharField(default=b'panel-default', max_length=13, choices=[(b'panel-default', b'Default'), (b'panel-primary', b'Primary'), (b'panel-success', b'Success'), (b'panel-warning', b'Warning'), (b'panel-danger', b'Danger'), (b'panel-info', b'Info')]),
        ),
    ]
