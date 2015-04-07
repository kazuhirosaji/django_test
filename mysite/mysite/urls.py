from django.conf.urls import patterns, include, url

from mysite.views import helloworld

urlpatterns = patterns('',
    url(r'^helloworld/', helloworld),
)
