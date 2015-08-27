from django.conf.urls import patterns, include, url
from django.contrib import admin
from library import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='query'),
    url(r'^$', views.index, name='book'),
    url(r'^confirm/$', views.confirm, name='confirm'),
    # url(r'^(?P<room_name>(man|woman))/$', views.man, name='room_name'),
    url(r'^man/$', views.ManListView.as_view(), name='man_room'),
    url(r'^woman/$', views.WomanListView.as_view(), name='woman_room'),
    # url(r'^woman_room/$', views.man_room, name='woman_room'),
)
