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
	url(r'^$', index),
	url(r'^about/$', about),
	url(r'^projects/$', projects),
	url(r'^members/$', members),
	url(r'^events/$', events),	
	url(r'^gallery/$', gallery),
	url(r'^login/$', login),
	url(r'^links/$', links),
 upstream/master
)
