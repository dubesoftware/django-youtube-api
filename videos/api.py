from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from videosite.settings import YOUTUBE_API_KEY as youtube_api_key

from videos.models import Video

import urlparse
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
		Override hydrate so we use the video link to pull the YouTube page using python-requests\
		and parse it for the video title and video description to be saved.

		OAuth authentication is not required as we are not retrieving user data.
		'''		
		video_link = bundle.data['video_link']
		if video_link:
			split_url = urlparse.urlsplit(video_link)
			url_query_dict = urlparse.parse_qs(split_url.query)
			video_id = url_query_dict['v'][0]
			video_api_url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet&fields=items(snippet/title,snippet/description)' % (video_id, youtube_api_key)
			try:
				video_request = requests.get(video_api_url)
				video_metadata = video_request.json()
				bundle.obj.video_title, bundle.obj.video_description = video_metadata['items'][0]['snippet']['title'], video_metadata['items'][0]['snippet']['description']				
			except Exception, e:
				print e.message
			finally:
				return bundle