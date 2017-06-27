#coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^jiaowu/$', views.jiaowu, name='jiaowu'),
    # 教务、学生、教师页头部
	url(r'^header.html$', views.header, name = 'header'),
]