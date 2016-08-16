from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Add_User
from ..loginreg.models import User
from ..courses.models import Course
from django.db.models import Count

# Create your views here.
def index(request):
	context = {
		'courses': Course.objects.all()
		}
	return render(request, "courses/index.html", context)

def login(request):
	context = {
		'users': User.objects.all()
		}
	return render(request, "loginreg/index.html", context)

def new_user(request):
	""" Name stuff consistently! """
	context = {
		'courses': Course.objects.all().annotate(courseusers = Count("courses")),
		'users': User.objects.all()
		}
	return render(request, "integrate/index.html", context)

def add_new(request):
	""" What are you doing with this context object?

	context = {
		'courses': Course.objects.all().annotate(usercourse=Count('add_user__user')),
		'users': User.objects.all()
		}
	"""
	user = User.objects.get(id=request.POST['userid'])
	course = Course.objects.get(id=request.POST['courseid'])
	"""
	add a user to course
	"""
	Add_User.objects.create(course_id=course.id, user_id=user.id)
	"""
	printed all added users here.
	"""
	print Add_User.objects.all()

	return redirect('/add_user')
