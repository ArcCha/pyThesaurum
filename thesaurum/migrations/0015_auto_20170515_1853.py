# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurum', '0014_auto_20170515_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grading',
            old_name='first_question',
            new_name='cost_justified',
        ),
        migrations.RenameField(
            model_name='grading',
            old_name='fourth_question',
            new_name='cost_rational',
        ),
        migrations.RenameField(
            model_name='grading',
            old_name='second_question',
            new_name='project_justified',
        ),
        migrations.RenameField(
            model_name='grading',
            old_name='third_question',
            new_name='project_rational',
        ),
    ]