# coding: utf-8
from django.conf.urls import url
from django.contrib.auth import views
from django.core.urlresolvers import reverse_lazy

from .views import BugListView, BugDetailView, RegisterView, BugCreateView

urlpatterns = [
    url(r'^$', BugListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', BugDetailView.as_view(), name='detail'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', views.login, {"template_name" : "bugtracker/login.html"}, name="login"),
    url(r'^logout/$', views.logout, {"next_page" : reverse_lazy('login')}, name="logout"),
    url(r'^add/$', BugCreateView.as_view(), name='add'),
]
