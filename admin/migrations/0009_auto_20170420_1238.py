# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0008_auto_20161124_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='activated',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='admin_activation',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='associated_groups',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='mail_confirmation',
        ),
    ]
