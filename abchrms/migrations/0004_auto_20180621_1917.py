# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abchrms', '0003_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='marriage_anniv',
            field=models.DateField(null=True),
        ),
    ]
