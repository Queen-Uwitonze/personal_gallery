# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20190319_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='images_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
        ),
    ]
