from django.conf.urls import patterns, include, url
from testblog import views
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib.comments import urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.login),
    url(r'^main/$', views.main),
    url(r'^profile/$', views.profile),
    url(r'^registration/$',  views.register),
    url(r'^post/(?P<id>\d+)/$', views.view_post, name='View_post'),
    url(r'^logout/$', views.logout),
    url(r"^addpost/$", views.addpost),
    url(r'^changeprofile/$', views.changeprofile),   
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/(?P<id>\d+)/myposts/$', views.myposts, name='myposts'),
)
