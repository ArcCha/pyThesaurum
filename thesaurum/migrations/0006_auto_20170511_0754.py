# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurum', '0005_auto_20170511_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='previous_subsidy',
            field=models.DecimalField(blank=True, decimal_places=2, default=10.12, max_digits=10),
        ),
    ]