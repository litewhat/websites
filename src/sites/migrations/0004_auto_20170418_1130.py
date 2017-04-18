# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20170418_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='meta_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='website',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.WebsiteCategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='website',
            name='meta_description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
