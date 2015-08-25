__author__ = 'babayega'
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^storyoftheweek/$', views.storyoftheweek, name='storyoftheweek'),
    url(r'^books/$', views.books, name='books'),
    url(r'^videos/$', views.videos, name='videos'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]