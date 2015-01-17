from django.conf.urls import patterns, include, url
from sales import views

urlpatterns = patterns('',
    url(r'^charge/$', views.charge, name="charge"),
)
