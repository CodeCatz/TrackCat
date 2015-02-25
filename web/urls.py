from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='pages-index'),
	url(r'^about/$', views.about, name='pages-about'),
	url(r'^projects/$', views.projects, name='pages-projects'),
	url(r'^tasks/$', views.tasks, name='pages-tasks'),
	url(r'^tasks/(?P<task_id>[0-9]+)/edit/$', views.task_edit, name='task-edit'),
	url(r'^tasks/new/$', views.task_new, name='task-new'),
	url(r'^members/$', views.members, name='pages-members'),
	url(r'^member-page/(?P<user_id>[0-9]+)/$', views.member_page, name='pages-member-detail'),
	url(r'^edituser/$', views.user_edit, name='pages-edit-user'),
	url(r'^events/$', views.events, name='pages-events'),
	url(r'^gallery/$', views.gallery, name='pages-gallery'),
	url(r'^login/$', views.login, name='pages-login'),
	url(r'^links/$', views.links, name='pages-links'),
	url(r'^privacy/$', views.privacy, name='pages-privacy'),
	url(r'^project/(?P<project_id>[0-9]+)/$',views.project_detail, name='project-detail'),
	url(r'^project/new/$', views.project_new, name='project-new'),
	url(r'^project/(?P<project_id>[0-9]+)/edit/$', views.project_edit, name='project-edit'),
	url(r'^logout/$', views.logout, name='logout'),
)
