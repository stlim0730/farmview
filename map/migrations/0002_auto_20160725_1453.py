# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='dropbox_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='import_id',
            field=models.CharField(max_length=200),
        ),
    ]
