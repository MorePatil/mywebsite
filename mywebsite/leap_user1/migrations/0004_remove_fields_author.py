# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 11:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leap_user1', '0003_auto_20170521_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fields',
            name='author',
        ),
    ]
