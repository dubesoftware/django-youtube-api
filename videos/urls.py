from django.conf.urls import patterns, url

from videos import views

urlpatterns = patterns('',
	url(r'^video/$', views.get_video_list, name='get_video_list'),
	url(r'^video/(?P<video_id>\w+)/$', views.get_video, name='get_video'),
	url(r'^video/(?P<video_json>\w+)/$', views.post_video, name='post_video'),
	url(r'^video/(?P<video_id>\w+)/delete/$', views.delete_video, name='delete_video'),
)
