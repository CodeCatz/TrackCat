# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150304_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='website',
            field=models.URLField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'OPENED', max_length=15, choices=[(b'OPENED', b'Opened'), (b'INPROGRESS', b'In progress'), (b'CLOSED', b'Closed'), (b'DELETED', b'Deleted')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_id',
            field=models.ForeignKey(related_name='assignee', blank=True, to='api.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='owner_id',
            field=models.ForeignKey(related_name='owner', to='api.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'UNASSIGNED', max_length=15, choices=[(b'UNASSIGNED', b'Unassigned'), (b'ASSIGNED', b'Assigned'), (b'WORKINGON', b'Working On'), (b'COMPLETED', b'Completed'), (b'DELETED', b'Deleted')]),
            preserve_default=True,
        ),
    ]
