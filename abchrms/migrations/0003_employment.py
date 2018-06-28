# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('abchrms', '0002_auto_20180621_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_email_id', models.EmailField(max_length=254)),
                ('doj', models.DateField()),
                ('job_band', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('emp_type', models.CharField(max_length=20)),
                ('confirmation_status', models.CharField(max_length=20)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('notice_period_in_months', models.IntegerField()),
                ('department', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
                ('creation_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abchrms.Employee')),
                ('hr_manager_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HRManager', to='abchrms.Employee')),
                ('reporting_manager_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ReportingManager', to='abchrms.Employee')),
            ],
        ),
    ]
