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
            field=models.CharField(default=b'OPENED', max_length=15, choices=[(b'OPENED', b'Opened'), (b'INPROGRESS', b'In progress'), (b'CLOSED', b'Closed')]),
            preserve_default=True,
        ),
    ]
