# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vizjson_url', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('optional_note', models.CharField(max_length=200)),
            ],
        ),
    ]
