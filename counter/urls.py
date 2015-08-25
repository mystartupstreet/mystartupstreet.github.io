__author__ = 'babayega'

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.counter),
    url(r'^thanks/$', views.thanks, name='thanks'),


]