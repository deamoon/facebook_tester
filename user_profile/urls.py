from django.conf.urls import patterns, url
from user_profile import views

urlpatterns = patterns(
    '',
    url(r'^$', views.profile, name='user_profile'),
)
