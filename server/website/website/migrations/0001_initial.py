# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-13 06:38
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_knobs', models.TextField()),
                ('raw_initial_metrics', models.TextField()),
                ('raw_final_metrics', models.TextField()),
                ('raw_summary', models.TextField()),
                ('knob_log', models.TextField()),
                ('metric_log', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DBMSCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, b'MySQL'), (2, b'Postgres'), (3, b'Db2'), (4, b'Oracle'), (5, b'SQL Server'), (6, b'SQLite'), (7, b'HStore'), (8, b'Vector')])),
                ('version', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, b'generic'), (2, b't2.nano'), (3, b't2.micro'), (4, b't2.small'), (5, b't2.medium'), (6, b't2.large'), (7, b't2.xlarge'), (8, b't2.2xlarge'), (9, b'm4.large'), (10, b'm4.xlarge'), (11, b'm4.2xlarge'), (12, b'm4.4xlarge'), (13, b'm4.10xlarge'), (14, b'm4.16xlarge'), (15, b'm3.medium'), (16, b'm3.large'), (17, b'm3.xlarge'), (18, b'm3.2xlarge'), (19, b'c4.large'), (20, b'c4.xlarge'), (21, b'c4.2xlarge'), (22, b'c4.4xlarge'), (23, b'c4.8xlarge'), (24, b'c3.large'), (25, b'c3.xlarge'), (26, b'c3.2xlarge'), (27, b'c3.4xlarge'), (28, b'c3.8xlarge'), (29, b'p2.xlarge'), (30, b'p2.8xlarge'), (31, b'p2.16xlarge'), (32, b'g2.2xlarge'), (33, b'g2.8xlarge'), (34, b'x1.16large'), (35, b'x1.32xlarge'), (36, b'r4.large'), (37, b'r4.xlarge'), (38, b'r4.2xlarge'), (39, b'r4.4xlarge'), (40, b'r4.8xlarge'), (41, b'r4.16xlarge'), (42, b'r3.large'), (43, b'r3.xlarge'), (44, b'r3.2xlarge'), (45, b'r3.4xlarge'), (46, b'r3.8xlarge'), (47, b'i3.large'), (48, b'i3.xlarge'), (49, b'i3.2xlarge'), (50, b'i3.4xlarge'), (51, b'i3.8xlarge'), (52, b'i3.16large'), (53, b'd2.xlarge'), (54, b'd2.2xlarge'), (55, b'd2.4xlarge'), (56, b'd2.8xlarge'), (57, b'f1.2xlarge'), (58, b'f1.16xlarge')])),
                ('name', models.CharField(max_length=32)),
                ('cpu', models.IntegerField()),
                ('memory', models.FloatField()),
                ('storage', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('storage_type', models.CharField(max_length=16)),
                ('additional_specs', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KnobCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('vartype', models.IntegerField(choices=[(1, b'STRING'), (2, b'INTEGER'), (3, b'REAL'), (4, b'BOOL'), (5, b'ENUM'), (6, b'TIMESTAMP')], verbose_name=b'variable type')),
                ('unit', models.IntegerField(choices=[(1, b'bytes'), (2, b'milliseconds'), (3, b'other')])),
                ('category', models.TextField(null=True)),
                ('summary', models.TextField(null=True, verbose_name=b'description')),
                ('description', models.TextField(null=True)),
                ('scope', models.CharField(max_length=16)),
                ('minval', models.CharField(max_length=32, null=True, verbose_name=b'minimum value')),
                ('maxval', models.CharField(max_length=32, null=True, verbose_name=b'maximum value')),
                ('default', models.TextField(verbose_name=b'default value')),
                ('enumvals', models.TextField(null=True, verbose_name=b'valid values')),
                ('context', models.CharField(max_length=32)),
                ('tunable', models.BooleanField(verbose_name=b'tunable')),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KnobData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField()),
                ('data', models.TextField()),
                ('knobs', models.TextField()),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetricCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('vartype', models.IntegerField(choices=[(1, b'STRING'), (2, b'INTEGER'), (3, b'REAL'), (4, b'BOOL'), (5, b'ENUM'), (6, b'TIMESTAMP')])),
                ('summary', models.TextField(null=True, verbose_name=b'description')),
                ('scope', models.CharField(max_length=16)),
                ('metric_type', models.IntegerField(choices=[(1, b'COUNTER'), (2, b'INFO')])),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetricData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField()),
                ('data', models.TextField()),
                ('metrics', models.TextField()),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PipelineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(choices=[(1, b'Pruned Metrics'), (2, b'Ranked Knobs'), (3, b'Aggregated Data'), (4, b'Workload Mapping Data'), (5, b'Knob Data'), (6, b'Metric Data')])),
                ('data', models.TextField()),
                ('creation_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PipelineResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_timestamp', models.DateTimeField()),
                ('task_type', models.IntegerField(choices=[(1, b'Pruned Metrics'), (2, b'Ranked Knobs'), (3, b'Aggregated Data'), (4, b'Workload Mapping Data'), (5, b'Knob Data'), (6, b'Metric Data')])),
                ('value', models.TextField()),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
                ('hardware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Hardware')),
            ],
            options={
                'get_latest_by': 'creation_timestamp',
            },
        ),
        migrations.CreateModel(
            name='PipelineRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name=b'project name')),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_time', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('observation_start_time', models.DateTimeField()),
                ('observation_end_time', models.DateTimeField()),
                ('observation_time', models.FloatField()),
                ('task_ids', models.CharField(max_length=180, null=True)),
                ('next_configuration', models.TextField(null=True)),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
                ('knob_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.KnobData')),
                ('metric_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.MetricData')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name=b'session name')),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_time', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('upload_code', models.CharField(max_length=30, unique=True)),
                ('tuning_session', models.BooleanField()),
                ('target_objective', models.CharField(max_length=64, null=True)),
                ('nondefault_settings', models.TextField(null=True)),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
                ('hardware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Hardware')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name=b'workload name')),
                ('dbms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.DBMSCatalog')),
                ('hardware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Hardware')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='result',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Session', verbose_name=b'session name'),
        ),
        migrations.AddField(
            model_name='result',
            name='workload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Workload'),
        ),
        migrations.AddField(
            model_name='pipelinedata',
            name='pipeline_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.PipelineRun'),
        ),
        migrations.AddField(
            model_name='pipelinedata',
            name='workload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Workload'),
        ),
        migrations.AddField(
            model_name='metricdata',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Session'),
        ),
        migrations.AddField(
            model_name='knobdata',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Session'),
        ),
        migrations.AddField(
            model_name='backupdata',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Result'),
        ),
        migrations.AlterUniqueTogether(
            name='pipelineresult',
            unique_together=set([('dbms', 'hardware', 'creation_timestamp', 'task_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='pipelinedata',
            unique_together=set([('pipeline_run', 'task_type', 'workload')]),
        ),
    ]
