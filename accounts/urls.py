from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from accounts.views import DonorCreateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url('^register/', DonorCreateView.as_view()),
)
