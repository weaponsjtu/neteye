from django.conf.urls.defaults import *
#from pinax.apps.account import urls

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from wangji.sharesite.models import Onesite

info_dict = {
	'queryset': Onesite.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^wangji/', include('wangji.foo.urls')),
    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

	(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT, 'show_indexes': True}),

	#(r"^account/", include("pinax.apps.account.urls")),
	(r'^account/', include('wangji.account.urls')),
	(r'^people/', include('wangji.people.urls')),
	(r'^sharesite/', include('wangji.sharesite.urls')),
    (r'^(?P<tag_id>\d+)/$', 'wangji.sharesite.views.tag'),
	(r'^siteinfo/$', 'wangji.sharesite.option.siteinfo'),
	(r'^$', 'wangji.sharesite.views.index'),

	(r'^snooker/$', 'wangji.sharesite.snooker.snooker'),
	(r'^sjtu/$', 'wangji.sharesite.snooker.index'),
	(r'^invite/$', 'wangji.sharesite.snooker.invite'),
	(r'^snooker/about/$', 'wangji.sharesite.snooker.about'),
	(r'^snooker/players/$', 'wangji.sharesite.snooker.players'),
	(r'^snooker/clubs/$', 'wangji.sharesite.snooker.clubs'),
	(r'^snooker/voice/$', 'wangji.sharesite.snooker.voice'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)


