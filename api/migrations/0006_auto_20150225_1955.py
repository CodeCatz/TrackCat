# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='status_id',
            new_name='status',
        ),
    ]
