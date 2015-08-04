from django.conf.urls import patterns, url
from check_app_version import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eag_lib.views.home', name='home'),
    url(r'^(?P<app_id>\w+)', views.check_version, name='check_version'),
)
