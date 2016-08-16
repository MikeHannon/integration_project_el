from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg_process$', views.reg, name='reg'),
    url(r'^log_process$', views.log),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]
