# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-16 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_remove_notification_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='read',
        ),
    ]
