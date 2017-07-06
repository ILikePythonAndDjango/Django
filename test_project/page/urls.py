from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',
	#url(r'^$', views.index, name = "index"),
	#url(r'^good', views.good, name = "good"),
	url(r'^(?:\?id=(?P<id>\d+))?$', views.index, name = "index"),
	url(r'^good/\?id=(?P<id>\d+)$', views.good, name = "good")
)