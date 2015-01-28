# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(serialize=False, primary_key=True)),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.CharField(max_length=150, blank=True)),
                ('status_id', models.CharField(default=b'OPENED', max_length=8, choices=[(b'OPENED', b'Opened'), (b'INPROGRESS', b'In progress'), (b'CLOSED', b'Closed')])),
                ('project_deadline', models.DateTimeField(blank=True)),
                ('repository_link', models.URLField(max_length=300)),
                ('website_production', models.URLField(max_length=300, blank=True)),
                ('website_test', models.URLField(max_length=300, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('status', models.CharField(default=b'UNASSIGNED', max_length=15, choices=[(b'UNASSIGNED', b'Unassigned'), (b'ASSIGNED', b'Assigned'), (b'WORKINGON', b'Working On'), (b'COMPLETED', b'Completed')])),
                ('deadline', models.DateTimeField(null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('assigned_id', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=100)),
                ('githubuser', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('profile_picture', models.ImageField(upload_to=b'', blank=True)),
                ('website', models.URLField()),
                ('bio', models.TextField(max_length=2000, blank=True)),
                ('active', models.BooleanField(default=False)),
                ('activity_status', models.CharField(max_length=2, choices=[(b'SC', b'Sleepy_Cat'), (b'LC', b'Lazy_Cat'), (b'AC', b'Active_Cat'), (b'MC', b'Mentor_Cat')])),
                ('last_logged_in', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='owner_id',
            field=models.ForeignKey(to='api.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='project_id',
            field=models.ForeignKey(to='api.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='project_owner',
            field=models.ForeignKey(to='api.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='user_project',
            field=models.ManyToManyField(related_name='user_project', to='api.UserProfile'),
            preserve_default=True,
        ),
    ]
