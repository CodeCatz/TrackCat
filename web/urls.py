from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='pages-index'),
	url(r'^about/$', views.about, name='pages-about'),
	url(r'^projects/$', views.projects, name='pages-projects'),
	url(r'^members/$', views.members, name='pages-members'),
	url(r'^events/$', views.events, name='pages-events'),
	url(r'^gallery/$', views.gallery, name='pages-gallery'),
	url(r'^login/$', views.login, name='pages-login'),
	url(r'^links/$', views.links, name='pages-links'),
	url(r'^edituser/$', views.edituser, name='pages-edituser'),
	url(r'^privacy/$', views.privacy, name='pages-privacy'),
	url(r'^project/(?P<project_id>[0-9]+)/$', views.project_detail),
	url(r'^project/new/$', views.project_new, name='project_new'),
	url(r'^project/(?P<project_id>[0-9]+)/edit/$', views.project_edit, name='project_edit'),
)
