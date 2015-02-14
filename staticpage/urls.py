from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', 'staticpage.views.index_main', name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='staticpage/about.html'), name="about"),
)
