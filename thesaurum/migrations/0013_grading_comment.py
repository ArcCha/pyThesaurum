# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurum', '0012_auto_20170515_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='grading',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
