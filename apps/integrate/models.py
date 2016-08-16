from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User
from ..courses.models import Course

# Create your models here.
class Add_User(models.Model):
	user = models.ForeignKey(User, related_name="users")
	course = models.ForeignKey(Course, related_name="courses")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
