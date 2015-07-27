from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eag_lib.views.home', name='home'),
    url(r'^library/', include('library.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
