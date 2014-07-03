# Create your views here.
# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage

import time
import datetime
import string
import random

from wangji.sharesite.models import Onesite, Comments

def index(request):
	latest_onesite_list = Onesite.objects.all().order_by('-pub_date')
	sitenum = latest_onesite_list.count()
	randnum = random.randint(0, sitenum - 2) + 2 ;	

	
	#popular_onesite_list = Onesite.objects.all().order_by('-pub_date')
	#.order_by('-pub_date')[:5]
	paginator = Paginator(latest_onesite_list, 10)
	#make sure page request is an int.If not, deliver first page.	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	# If page request(9999) is out of range. deliver the last page
	try:
		contacts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		contacts = paginator.page(paginator.num_pages)

	if not request.user.is_authenticated():
		#print user.username
		label1 = '登录'
		label2 = '/account/'
		label3 = '注册'
		label4 = '/account/register/'
		return render_to_response('sharesite/onesite_list.html', {'objectlist': contacts, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'randnum': randnum}, context_instance=RequestContext(request))
	else:
		#print 'hello'
		obj = User.objects.get(username = request.user.username)
		label1 = obj.username
		label2 = '/people/%d' % (obj.id,)
		label3 = '退出'
		label4 = '/account/signup'
		label5 = '我的空间'
		return render_to_response('sharesite/onesite_list.html', {'objectlist': contacts, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'label5': label5,'randnum': randnum}, context_instance=RequestContext(request))
		#return render_to_response('sharesite/siteinfo.html', context_instance=RequestContext(request))
	#t = loader.get_template('sharesite/index.html')
	#c = Context({
	#	'latest_onesite_list':latest_onesite_list,
	#})
	#return HttpResponse(t.render(c))
	#return render_to_response('sharesite/onesite_list.html', {'object_list': latest_onesite_list})

	# site tags
def tag(request, tag_id):
	 
	sitenum = Onesite.objects.all().count()
	randnum = random.randint(0, sitenum - 2) + 2 ;

	Tags = ['game', 'music', 'video', 'study', 'life', 'others']
	latest_onesite_list = Onesite.objects.filter( tags__startswith=Tags[int(tag_id)] ).order_by('-pub_date')
	# display by each page	
	paginator = Paginator(latest_onesite_list, 10)
	#make sure page request is an int.If not, deliver first page.	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	# If page request(9999) is out of range. deliver the last page
	try:
		contacts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		contacts = paginator.page(paginator.num_pages)
	
	if not request.user.is_authenticated():
		label1 = '登录'
		label2 = '/account/'
		label3 = '注册'
		label4 = '/account/register/'
		return render_to_response('sharesite/onesite_list.html', {'objectlist': contacts, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'randnum': randnum}, context_instance=RequestContext(request))
	else:
		obj = User.objects.get(username = request.user.username)
		label1 = obj.username
		label2 = '/people/%d' % (obj.id,)
		label3 = '退出'
		label4 = '/account/signup'
		label5 = '我的空间'
		return render_to_response('sharesite/onesite_list.html', {'objectlist': contacts, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'label5': label5,'randnum': randnum}, context_instance=RequestContext(request))

	# search result 
def result(request):
	sitenum = Onesite.objects.all().count()
	randnum = random.randint(0, sitenum - 2) + 2 ;

	querys = request.POST["searchbox"]
	latest_onesite_list = Onesite.objects.filter( info__contains = querys ).order_by('-pub_date')
	# display by each page	
	paginator = Paginator(latest_onesite_list, 10)
	#make sure page request is an int.If not, deliver first page.	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	# If page request(9999) is out of range. deliver the last page
	try:
		contacts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		contacts = paginator.page(paginator.num_pages)
	
	if not request.user.is_authenticated():
		label1 = '登录'
		label2 = '/account/'
		label3 = '注册'
		label4 = '/account/register/'
		return render_to_response('sharesite/onesite_list.html', {'objectlist': contacts, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'randnum': randnum}, context_instance=RequestContext(request))
	else:
		obj = User.objects.get(username = request.user.username)
		label1 = obj.username
		label2 = '/people/%d' % (obj.id,)
		label3 = '退出'
		label4 = '/account/signup'
		label5 = '我的空间'
		return render_to_response('sharesite/onesite_list.html', {'objectlist': contacts, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'label5': label5, 'randnum': randnum}, context_instance=RequestContext(request))


def detail(request, onesite_id):
	#try:
	#	p = Onesite.objects.get(pk = onesite_id)
	#except Onesite.DoesNotExist:
	#	raise Http404
	p = get_object_or_404(Onesite, pk = onesite_id)
	#return render_to_response('sharesite/onesite_detail.html',{'object':p}, context_instance=RequestContext(request))
	if not request.user.is_authenticated():
		label1 = '登录'
		label2 = '/account/'
		label3 = '注册'
		label4 = '/account/register/'
		return render_to_response('sharesite/onesite_detail.html', {'object': p, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4}, context_instance=RequestContext(request))
	else:
		obj = User.objects.get(username = request.user.username)
		label1 = obj.username
		label2 = '/people/%d' % (obj.id,)
		label3 = '退出'
		label4 = '/account/signup'
		label5 = '我的空间'
		return render_to_response('sharesite/onesite_detail.html', {'object': p, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'label5': label5}, context_instance=RequestContext(request))
#	#return HttpResponse("You are looking at the detail of site %s" % onesite_id)

def info(request, object_id):
	try:
		object_id = int(object_id)
	except ValueError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours=object_id)
	assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(object_id,dt)
	return HttpResponse(html);	
#	return HttpResponse("You are looking at the info of site %s" % onesite_id)
#
#def comments(request, onesite_id):
#	return HttpResponse("You are looking at the comments of site %s" % onesite_id)

def evaluate(request, object_id):
	p = get_object_or_404(Onesite, pk=object_id)
	if not request.user.is_authenticated():
		c = Comments(user='anonymous',star=3,agree=1,content=request.POST['comment'])
		c.onesite = p
		c.pub_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  
		c.save()
		label1 = '登录'
		label2 = '/account/'
		label3 = '注册'
		label4 = '/account/register/'
		return render_to_response('sharesite/onesite_detail.html', {'object': p, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4}, context_instance=RequestContext(request))
	else:
		c = Comments(user=request.user.username,star=3,agree=1,content=request.POST['comment'])
		c.onesite = p
		c.pub_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  
		c.save()
		obj = User.objects.get(username = request.user.username)
		label1 = obj.username
		label2 = '/people/%d' % (obj.id,)
		label3 = '退出'
		label4 = '/account/signup'
		label5 = '我的空间'
		return render_to_response('sharesite/onesite_detail.html', {'object': p, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4, 'label5': label5}, context_instance=RequestContext(request))
		
	
	# Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
	#return HttpResponseRedirect(reverse('onesite_detail', args=(p.id,)))

def add(request, object_id):
	return render_to_response('sharesite/site_add.html', {'objectid':object_id}, context_instance=RequestContext(request))
	




