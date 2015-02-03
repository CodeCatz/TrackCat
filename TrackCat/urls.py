from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import User

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('web.urls')),
	url('', include('social_auth.urls')),
)

