from django.conf.urls.defaults import *
from wangji.sharesite.models import Onesite

info_dict = {
	'queryset': Onesite.objects.all(),		
}

urlpatterns = patterns('',
	#(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
	(r'^(?P<onesite_id>\d+)/$', 'wangji.sharesite.views.detail'),
	#(r'^(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',info_dict),
	url(r'^(?P<object_id>\d+)/detail/$','django.views.generic.list_detail.object_detail',dict(info_dict,template_name='sharesite/onesite_detail.html'),'onesite_detail'),
	(r'^(?P<object_id>\d+)/evaluate/$','wangji.sharesite.views.evaluate'),
	(r'^(?P<object_id>\d+)/info/$','wangji.sharesite.views.info'),
	(r'^(?P<object_id>\d+)/add/$', 'wangji.sharesite.views.add'),
	(r'^(?P<object_id>\d+)/share/$', 'wangji.sharesite.option.share'),
	(r'^addsite/$', 'wangji.sharesite.option.addsite'),
	(r'^result/$', 'wangji.sharesite.views.result'),
	(r'^$', 'wangji.sharesite.views.index'),
	#(r'^/(?P<page_id>\d+)/$$', 'wangji.sharesite.views.index'),
)

#urlpatterns = patterns('wangji.sharesite.views',
#	(r'^$', 'index'),	
#	(r'^(?P<onesite_id>\d+)/$', 'detail'),
#	(r'^(?P<onesite_id>\d+)/info/$', 'info'),
#	(r'^(?P<onesite_id>\d+)/comments/$', 'comments'),
#	(r'^(?P<onesite_id>\d+)/evaluate/$', 'evaluate'),
#)
