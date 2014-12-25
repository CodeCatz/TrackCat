from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from TrackCat.views import index, about #dodala Petra
=======
from TrackCat.views import index, projects
>>>>>>> upstream/master

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackCat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
<<<<<<< HEAD
    url(r'^about/$', about),
=======
    url(r'^projects/$', projects),
>>>>>>> upstream/master
)


