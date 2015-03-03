# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150225_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activity_status',
            field=models.CharField(choices=[('KITTEN', 'New Kitten'), ('ACTIVE', 'Active Cat'), ('SLEEPY', 'Sleepy Cat'), ('MENTOR', 'Mentor Cat')], max_length=50, default='KITTEN'),
            preserve_default=True,
        ),
    ]
