from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import piano.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^piano$', piano.views.index),
    url(r'^piano/play$', piano.views.play),
    url(r'^piano/get$', piano.views.get),
    url(r'^light$', hello.views.light, name='light'),
    # url(r'^light_edit$', hello.views.light_edit, name='light_edit'),
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
