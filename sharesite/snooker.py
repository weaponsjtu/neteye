from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
import time, string


def snooker(request):
    u = get_object_or_404(User, pk=15)
    messages = u.messageboard_set.all().order_by('-pub_date')
    return render_to_response('snooker/championship.html', {'messages':messages},context_instance=RequestContext(request))

def index(request):
    return render_to_response('snooker/index.html', context_instance=RequestContext(request))

def invite(request):
    return render_to_response('snooker/invite.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('snooker/about.html', context_instance=RequestContext(request))

def players(request):
    return render_to_response('snooker/players.html', context_instance=RequestContext(request))

def clubs(request):
    return render_to_response('snooker/clubs.html', context_instance=RequestContext(request))

def voice(request):
    return render_to_response('snooker/voice.html', context_instance=RequestContext(request))
