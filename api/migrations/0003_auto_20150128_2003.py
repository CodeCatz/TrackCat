# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150128_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_deadline',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
