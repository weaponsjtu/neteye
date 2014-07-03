from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'wangji.account.views.index'),
	(r'^signin/$', 'wangji.account.views.signin'),
	(r'^signup/$', 'wangji.account.views.signup'),
	(r'^resetpassword/$', 'wangji.account.views.resetpassword'),
	(r'^register/$', 'wangji.account.views.register'),
	(r'^registerUser/$', 'wangji.account.views.registerUser'),
)
