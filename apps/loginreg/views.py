from django.shortcuts import render, redirect, HttpResponse
from .models import User
from datetime import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	return render(request, "loginreg/index.html")
def success(request):
	return render(request, "loginreg/success.html")
def reg(request):
	errors = False
	namecheck = User.userManager.bothnames(request.POST['first_name'], request.POST['last_name'])
	emailcheck = User.userManager.email(request.POST['email'])
	passwordcheck = User.userManager.password(request.POST['password'])
	confirmpwcheck = User.userManager.confirm_password(request.POST['password'], request.POST['confirm_password'])
	confirmbday = User.userManager.birthday(request.POST['bday'])
	if namecheck[0] == False:
		messages.add_message(request, messages.INFO, namecheck[1], extra_tags='reg')
		errors = True
	if emailcheck[0] == False:
		messages.add_message(request, messages.INFO, emailcheck[1], extra_tags='reg')
		errors = True
	if passwordcheck[0] == False:
		messages.add_message(request, messages.INFO, passwordcheck[1], extra_tags='reg')
		errors = True
	if confirmbday[0] == False:
		messages.add_message(request, messages.INFO, confirmbday[1], extra_tags='reg')
		errors = True
		print confirmbday[1]
	if confirmpwcheck[0] == False:
		messages.add_message(request, messages.INFO, confirmpwcheck[1], extra_tags='reg')
		errors = True
	if errors == True:
		return redirect('/')
	else:
		User.objects.create(first_name = namecheck[1], last_name = namecheck[2], email = emailcheck[1], password = passwordcheck[1], birthday = confirmbday[1])
		messages.add_message(request, messages.INFO, "Successfully registered!")
		request.session['user'] = namecheck[1]
		print confirmbday[1]
		return redirect(reverse('index'))
def log(request):
	logcheck = User.userManager.trylogin(request.POST['email'], request.POST['password'])
	if logcheck[0] == False:
		messages.add_message(request, messages.INFO, logcheck[1], extra_tags='log')
		return redirect('/')
	else:
		request.session['user'] = logcheck[1]
		messages.add_message(request, messages.INFO, "Successfully logged in!")
		return redirect('/success')

def logout(request):
	del request.session['user']
	return redirect('/')
