from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from videos.models import Video

import requests

class VideoResource(ModelResource):
	class Meta:
		queryset = Video.objects.all()
		resource_name = 'video'
		excludes = ['video_title', 'video_description']
		allowed_methods = ['get', 'post', 'delete']
		authorization = Authorization()

	def hydrate(self, bundle):
		'''
		Override hydrate so we use the video link to pull the YouTube page using python-requests and parse it for the title 
		for the video title and video description to be saved.
		'''
		video_request = requests.get(bundle.obj.video_link)
		bundle.obj.video_title, bundle.obj.video_description = 'Testing...'
		return bundle