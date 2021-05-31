from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request,'login.html', c)

def newuser(request):
    name = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email_id = request.POST.get('email_id', '')
    user = User.objects.create_user(username=name,	password=password)
    user.save()
    return HttpResponseRedirect('/booking/ticketbook/')

    
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username,	password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/booking/ticketbook/')
	else:
		return HttpResponseRedirect('/loginmodule/login/')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
