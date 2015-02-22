# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150219_1527'),
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
            field=models.CharField(max_length=15, default='OPENED', choices=[('OPENED', 'Opened'), ('INPROGRESS', 'In progress'), ('CLOSED', 'Closed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=15, default='UNASSIGNED', choices=[('UNASSIGNED', 'Unassigned'), ('ASSIGNED', 'Assigned'), ('WORKINGON', 'Working On'), ('COMPLETED', 'Completed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activity_status',
            field=models.CharField(max_length=50, default='ACTIVE', choices=[('SLEEPY', 'Sleepy Cat'), ('LAZY', 'Lazy Cat'), ('ACTIVE', 'Active Cat'), ('MENTOR', 'Mentor Cat')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_picture', blank=True),
            preserve_default=True,
        ),
    ]
