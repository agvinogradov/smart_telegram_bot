# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodes_app', '0003_auto_20171206_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='sub_nodes',
        ),
        migrations.AddField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_nodes', to='nodes_app.Node'),
        ),
    ]