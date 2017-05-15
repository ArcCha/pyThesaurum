# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurum', '0011_auto_20170515_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('view_application', 'View application'), ('edit_application', 'Edit application'), ('grade_application', 'Can grade application'), ('change_application_state', 'Can change application state'))},
        ),
        migrations.AlterField(
            model_name='application',
            name='state',
            field=models.CharField(choices=[('new', 'New'), ('submitted', 'Submitted'), ('accepted', 'Accepted')], default='new', max_length=20),
        ),
    ]
