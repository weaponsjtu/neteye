# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_change
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def index(request):
	if not request.user.is_authenticated():
		return render_to_response('account/account_login.html', None, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('wangji.people.views.profile', args=(request.user.id,)))

def register(request):
	return render_to_response('account/account_register.html', None, context_instance=RequestContext(request))	

def registerUser(request):
	username = request.POST["form_name"]
	password = request.POST["form_password"]
	email = request.POST["form_email"]
	user = User.objects.create_user(username, email, password)
	user.is_staff = False
	user.save()
	return HttpResponseRedirect(reverse('wangji.people.views.profile', args=(user.id,)))

def signin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:	
			login(request, user)
			#return render_to_response('404.html', None,context_instance=RequestContext(request))
			return HttpResponseRedirect(reverse('wangji.sharesite.views.index', args=None))
			#to a login success html
		else:
			return render_to_response('500.html', None,context_instance=RequestContext(request))
	else:
		return render_to_response('403.html', None,context_instance=RequestContext(request))
def signup(request):
	logout(request)
	return HttpResponseRedirect(reverse('wangji.account.views.index', args=None))

def resetpassword(request):
	#password_change(request, 'account/account_resetpassword.html')
	return render_to_response('account/account_resetpassword.html', None, context_instance=RequestContext(request))
	#return HttpResponseRedirect(reverse('wangji.people.views.detail', args=(request.user.id,)))


