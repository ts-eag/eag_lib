from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from library import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eag_lib.views.home', name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^library/', include('library.urls')),
    url(r'^check_app_version/', include('check_app_version.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)