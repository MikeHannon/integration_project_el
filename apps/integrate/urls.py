from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add_user$', views.new_user, name = 'new_user'),
    url(r'^add_new$', views.add_new, name = 'add_new'),
    url(r'^login$', views.login, name = 'login'),
]