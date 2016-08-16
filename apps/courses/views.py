from django.shortcuts import render, redirect
from .models import Course
from ..loginreg.models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	# if you put the info in a form in a table, you can make it editable with route parameters like course.id - also would need to add name="update" on the urls page after views.update
	print User.objects.all()
	context = {
		'courses': Course.objects.all(),
		'users': User.objects.all()
	}
	return render(request, 'courses/index.html', context)
def add_course(request):
	print (request.POST)
	#this is the same as below but in one line:
	Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
	# same as above but broken down:
		# new_course = Course()
		# new_course.course_name = request.POST['course_name']
		# new_course.description = request.POST['description']
		# new_course.save()
	return redirect('/')

def delete(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	return redirect('/')

def delete_yes(request, id):
	context = {
		'course': Course.objects.get(id=id)
	}
	return render(request, 'courses/delete.html', context)
