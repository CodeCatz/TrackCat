from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='pages-index'),
	url(r'^about/$', views.about, name='pages-about'),
	url(r'^events/$', views.events, name='pages-events'),
	url(r'^login/$', views.login, name='pages-login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^members/$', views.members, name='pages-members'),
	url(r'^member/(?P<user_id>[0-9]+)/$', views.member_detail, name='pages-member-detail'),
	url(r'^member-edit/$', views.member_edit, name='pages-member-edit'),
	url(r'^projects/$', views.projects, name='pages-projects'),
	url(r'^project/(?P<project_id>[0-9]+)/$',views.project_detail, name='project-detail'),
	url(r'^project/new/$', views.project_new, name='project-new'),
	url(r'^project/(?P<project_id>[0-9]+)/edit/$', views.project_edit, name='project-edit'),
	url(r'^project/(?P<project_id>[0-9]+)/delete/$', views.project_delete, name='project-delete'),
	url(r'^tasks/$', views.tasks, name='pages-tasks'),
	url(r'^tasks/new/(?P<project_id>[0-9]+)/$', views.task_new, name='task-new'),
	url(r'^tasks/(?P<task_id>[0-9]+)/edit/$', views.task_edit, name='task-edit'),
	url(r'^tasks/(?P<task_id>[0-9]+)/delete/$', views.task_delete, name='task-delete'),
)
