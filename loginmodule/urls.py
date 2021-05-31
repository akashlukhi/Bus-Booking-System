from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^login/$', views.login),
	url(r'^auth/$', views.auth_view),
	url(r'^logout/$', views.logout),
	url(r'^newuser/$', views.newuser),
]
