# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=None, max_length=255)),
                ('start_date', models.DateTimeField()),
                ('location', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('organizer', models.CharField(default=None, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
