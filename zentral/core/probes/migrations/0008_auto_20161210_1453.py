# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probes', '0007_probesource_feed_probe_update_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='probesource',
            old_name='feed_probe_updated_at',
            new_name='feed_probe_last_synced_at',
        ),
    ]
