from django.conf.urls import patterns, include, url
from django.contrib import admin
from TrackCat.views import index, about #dodala Petra

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackCat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^about/$', about),
)


