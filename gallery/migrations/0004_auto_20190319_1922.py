# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20190319_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='images_name',
            field=models.CharField(max_length=30),
        ),
    ]
