from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import page_test.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
    url(r'', include('staticpage.urls', namespace="staticpage")),
    url(r'^page_test$', page_test.views.index),
    url(r'^page_test/add$', page_test.views.add),
    url(r'^accounts/', include('registration.backends.default.urls')), # django-registration
)
