from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from TrackCat.views import index
from TrackCat.views import projects
from TrackCat.views import login
=======
from TrackCat.views import index, about, projects, members, events, gallery, login, links
>>>>>>> upstream/master


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'TrackCat.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),


	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', index, name='pages-index'),
	url(r'^about/$', about, name='pages-about'),
	url(r'^projects/$', projects, name='pages-projects'),
	url(r'^members/$', members, name='pages-members'),
	url(r'^events/$', events, name='pages-events'),
	url(r'^gallery/$', gallery, name='pages-gallery'),
	url(r'^login/$', login, name='pages-login'),
	url(r'^links/$', links, name='pages-links'),
 upstream/master
)
