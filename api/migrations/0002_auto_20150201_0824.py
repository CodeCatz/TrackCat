# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status_id',
            field=models.CharField(choices=[('OPENED', 'Opened'), ('INPROGRESS', 'In progress'), ('CLOSED', 'Closed')], max_length=8, default='OPENED'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('UNASSIGNED', 'Unassigned'), ('ASSIGNED', 'Assigned'), ('WORKINGON', 'Working On'), ('COMPLETED', 'Completed')], max_length=15, default='UNASSIGNED'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activity_status',
            field=models.CharField(choices=[('SC', 'Sleepy_Cat'), ('LC', 'Lazy_Cat'), ('AC', 'Active_Cat'), ('MC', 'Mentor_Cat')], max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
    ]
