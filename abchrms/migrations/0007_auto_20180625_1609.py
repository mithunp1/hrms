# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abchrms', '0006_address_attendance_dependents_education_financials_leave_salary_transactons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year_of_passing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='annual_bonus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='basic',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='car_allow',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='education',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='hra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='lta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='others',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='pf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='special',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='vpay',
            field=models.FloatField(),
        ),
    ]
