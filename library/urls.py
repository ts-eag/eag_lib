from django.conf.urls import patterns, include, url
from django.contrib import admin
from library import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^man/$', views.man, name='man'),
    # url(r'^woman_room/$', views.man_room, name='woman_room'),
)
