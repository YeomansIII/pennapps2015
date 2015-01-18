from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.Home', name='home'),  
    url(r'^about/', 'app.views.About', name='about'),
    url(r'^privacy/', 'app.views.Privacy', name='privacy'),
    url(r'^pickup/', 'app.views.Pickup', name='pickup'),
    url(r'^tracking/', 'app.views.Tracking', name='tracking'),
    url(r'^profile/', 'app.views.Profile', name='profile')
)
