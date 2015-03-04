# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150228_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user_project',
        ),
        migrations.AddField(
            model_name='project',
            name='project_members',
            field=models.ManyToManyField(related_name='project_members', to='api.UserProfile'),
            preserve_default=True,
        ),
    ]
