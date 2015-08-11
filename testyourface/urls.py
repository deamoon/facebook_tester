from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import page_test.views
import user_profile.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('staticpage.urls', namespace="staticpage")),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')), # django-registration
    url(r'^page_test/', include('page_test.urls', namespace="page_test")),
    url(r'^users/', user_profile.views.main),
)
