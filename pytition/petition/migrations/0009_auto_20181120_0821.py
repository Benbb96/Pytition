# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-20 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0008_auto_20181114_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petition.Organization', verbose_name='Organization related to these permissions'),
        ),
    ]