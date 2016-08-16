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
	context = {
		'courses': Course.objects.all(),
		'users': User.objects.all()
		}
	return render(request, "integrate/index.html", context)

def add_new(request):
	context = {
		'courses': Course.objects.all().annotate(usercourse=Count('add_user__user')),
		'users': User.objects.all()
		}
	user = User.objects.get(id=request.POST['userid'])
	course = Course.objects.get(id=request.POST['courseid'])
	# print user.id
	# print course.id
	# new_user = Add_User.objects.create(course_id=course.id, user_id=user.id)
	# print taken_courses
	# for my_id in context['courses']:
	# 	# print my_id.id
	# 	taken_courses = Add_User.objects.filter(course_id=my_id.id)

	# 	print len(taken_courses)

	# print context['courses'][0].id
	# print new_user
	# get a count of users per course
		# show added count in number of users column
	return redirect('/add_user')