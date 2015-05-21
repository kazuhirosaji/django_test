from django.conf.urls import patterns, include, url

from mysite.views import helloworld
from mysite.views import mytemplate

# urlpatterns = patterns('',
#     url(r'^helloworld/', helloworld),
# )

urlpatterns = patterns('',
	('^templatetest1/$', mytemplate)
)
