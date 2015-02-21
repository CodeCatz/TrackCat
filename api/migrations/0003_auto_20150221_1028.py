# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150217_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='githubuser',
        ),
        migrations.AlterField(
            model_name='project',
            name='status_id',
            field=models.CharField(default='OPENED', choices=[('OPENED', 'Opened'), ('INPROGRESS', 'In progress'), ('CLOSED', 'Closed')], max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='UNASSIGNED', choices=[('UNASSIGNED', 'Unassigned'), ('ASSIGNED', 'Assigned'), ('WORKINGON', 'Working On'), ('COMPLETED', 'Completed')], max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activity_status',
            field=models.CharField(default='ACTIVE', choices=[('SLEEPY', 'Sleepy Cat'), ('LAZY', 'Lazy Cat'), ('ACTIVE', 'Active Cat'), ('MENTOR', 'Mentor Cat')], max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
    ]
