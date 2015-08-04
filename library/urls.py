from django.conf.urls import patterns, include, url
from django.contrib import admin
from library import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home'),
    url(r'^man_room/$', views.man_room, name='man_room'),
)
