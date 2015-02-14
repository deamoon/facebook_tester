from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # url(r'^$', views.contest_main, name='contest_main'),
    url(r'^(?P<company_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index),
    url(r'^add$', views.add),
)