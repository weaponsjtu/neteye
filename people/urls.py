from django.conf.urls.defaults import *
from wangji.people import views

urlpatterns = patterns('',
	#(r'^$', 'wangji.people.views.index'),
	(r'^(?P<object_id>\d+)/message/$', 'wangji.people.views.message'),
	(r'^(?P<object_id>\d+)/$', 'wangji.people.views.profile'),
	(r'^(?P<object_id>\d+)/(?P<shorsa>[a-z]{5})/$', 'wangji.people.views.detail'),
)

