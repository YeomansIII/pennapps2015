from django.conf.urls import patterns, include, url
from app import views


urlpatterns = patterns('',
    url(r'^$', views.Home, name='home'),
    url(r'^about/', views.About, name='about'),
    url(r'^privacy/', views.Privacy, name='privacy'),
    url(r'^pickup/', views.PickupPage, name='pickup'),
    url(r'^tracking/(?P<delivery_id>.+)$', views.Tracking, name='tracking'),
    url(r'^track/(?P<delivery_id>.+)$', views.TrackId, name='trackid'),
)
