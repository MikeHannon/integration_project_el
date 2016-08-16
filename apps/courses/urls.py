from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='course_home'),
    url(r'^add_course$', views.add_course, name='add_course'),
    url(r'^yes_delete/(?P<id>\d+)$', views.delete_yes),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    # url(r'^update/(?P<product.id>\d+$', views.update, name="update")
	    # from form in table
]

