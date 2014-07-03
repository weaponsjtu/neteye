from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
import time, string

from wangji.sharesite.models import Onesite


#   share the site
def	share(request, object_id):
	if not request.user.is_authenticated():
		return render_to_response('account/account_login.html', None, context_instance=RequestContext(request))
	else:
		userid = '*' + str(request.user.id) + '*'
		site = get_object_or_404(Onesite, pk=object_id)
		site.shareusers = str(site.shareusers) + userid
		site.save()
		return HttpResponseRedirect(reverse('wangji.sharesite.views.index', None))
#
##
#

#def

	# edit site
#def editsite(request, edit_id):


	# add site
def addsite(request):
	userid = request.POST["userid"]
	tags = request.POST["tags"]
	title = request.POST["saveTitle"]
	url = request.POST["saveURL"]
	logourl = request.POST["saveLogoURL"]
	info = request.POST["saveInfo"]
	skill = request.POST["saveSkill"]
	p = get_object_or_404(User, pk=userid)
	site = Onesite(user = p, tags = tags, title = title, logo = logourl, domain = url, value = "", info = info, skill = skill, pub_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	site.save()
	#return HttpResponseRedirect(reverse('wangji.people.views.detail', args=(userid,)))
	return HttpResponseRedirect(reverse('wangji.sharesite.views.index', None))


def	siteinfo(request):
	return render_to_response('sharesite/siteinfo.html', context_instance=RequestContext(request))

def snooker(request):
    u = get_object_or_404(User, pk=15)
    messages = u.messageboard_set.all().order_by('-pub_date')
    return render_to_response('sharesite/snooker.html', {'messages':messages},context_instance=RequestContext(request))
