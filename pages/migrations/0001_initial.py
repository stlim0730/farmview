# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('content', models.TextField(blank=True)),
                ('notice_type', models.CharField(default=b'panel-default', max_length=13, choices=[(b'panel-default', b'Default'), (b'panel-primary', b'Primary'), (b'panel-success', b'Success'), (b'panel-warning', b'Warning'), (b'panel-danger', b'Danger'), (b'panel-info', b'Info')])),
            ],
        ),
    ]
