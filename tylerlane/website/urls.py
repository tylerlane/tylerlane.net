from django.conf.urls.defaults import *

urlpatterns = patterns('website.views',
     url(r'/$','index',name='index'),
)

