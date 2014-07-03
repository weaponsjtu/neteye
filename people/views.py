# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from wangji.people.models import MessageBoard
from django.contrib.auth import logout
from wangji.sharesite.models import Onesite
import time, string

def index(request):
	object_list = User.objects.all().order_by('-date_joined')[:5]
	return render_to_response('people/people_list.html', {'object_list': object_list})

def profile(request, object_id):
	u = get_object_or_404(User, pk=object_id)
	site_list = u.onesite_set.all().order_by('-pub_date')
	return render_to_response('people/people_profile.html',{'object':u, 'site_list': site_list}, context_instance=RequestContext(request))

def detail(request,object_id, shorsa):
	u = get_object_or_404(User, pk=object_id)
	if (cmp(shorsa, 'saved') == 0):
		site_list = u.onesite_set.all().order_by('-pub_date')
		return render_to_response('people/people_profile.html',{'object':u, 'site_list': site_list}, context_instance=RequestContext(request))
	if (cmp(shorsa, 'share') == 0):
		site_list = Onesite.objects.filter( shareusers__contains = ('*' + str(u.id) + '*' )).order_by('-pub_date')
		return render_to_response('people/people_profile.html',{'object':u, 'site_list': site_list}, context_instance=RequestContext(request))


def message(request, object_id):
	p = get_object_or_404(User, pk=object_id)
	u = User()
	c = MessageBoard(user=u,star=3,agree=1,content=request.POST['info'])
	c.account = p
	c.pub_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	c.save()
	logout(request)
	return redirect('wangji.sharesite.snooker.snooker')
	# return render_to_response('sharesite/snooker.html',{'object':u}, context_instance=RequestContext(request))
	# return render_to_response('people/people_profile.html',{'object':u, 'site_list': site_list}, context_instance=RequestContext(request))
