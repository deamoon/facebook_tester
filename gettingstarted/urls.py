from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import piano.views
import page_test.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^piano$', piano.views.index),
    url(r'^piano/test1$', piano.views.test1),
    url(r'^piano/test2$', piano.views.test2),
    url(r'^piano/test3$', piano.views.test3),
    url(r'^piano/test4$', piano.views.test4),
    url(r'^piano/play$', piano.views.play),
    url(r'^piano/get$', piano.views.get),
    url(r'^light$', hello.views.light, name='light'),
    # url(r'^light_edit$', hello.views.light_edit, name='light_edit'),
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
    url(r'^page_test$', page_test.views.index),
)
