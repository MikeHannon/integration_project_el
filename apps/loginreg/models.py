from __future__ import unicode_literals

from django.db import models
from ..courses.models import Course
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
number_check = re.compile(r'^[a-zA-Z]+$')
import bcrypt
from datetime import datetime, date
# Create your models here.
class UserManager(models.Manager):
	def trylogin(self, email, password):
		try:
			user = User.objects.get(email = email)
		except:
			return (False, "User does not exist")
		password = password.encode()
		user_password = user.password.encode()
		if user and bcrypt.hashpw(password, user_password) == user_password:
			return (True, user.first_name)
		else:
			return (False, "Password does not match record")
		
	def bothnames(self, first_name, last_name):
		if len(first_name) > 1 and number_check.match(first_name) and len(last_name) > 1 and number_check.match(last_name):
			return (True, first_name, last_name)
		else:
			return(False, "Names must be no fewer than 2 characters and contain letters only")	
	def email(self, email):	
		if EMAIL_REGEX.match(email) and len(email) > 1:
			return(True, email)
		else:
			return(False, "Your email is invalid")
	def password(self, password):	
		if len(password) > 7:
			# BCRYPT PASSWORD 
			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			return (True, hashed)
		else:
			return(False, "Password must be no fewer than 8 characters")
	def confirm_password(self,password,confirm_password):
		if password == confirm_password:
			return (True, confirm_password)
		else:
			return (False, "Passwords must match")
	def birthday(self, birthday):
		bday_text = birthday
		now = datetime.now()
		bday_test = datetime.strptime(birthday, '%Y-%m-%d')
		if bday_test > now:
			return (False, "Birthday is invalid")
		else:
			return (True, birthday)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	birthday = models.DateField()
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()