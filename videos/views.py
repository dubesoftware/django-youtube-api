from django.shortcuts import render, HttpResponse

from videos.models import Video
# from videos.forms import VideoForm

def get_video_list(request):
	'''
	Returns a list of videos.
	'''
	video_list = Video.objects.all()

	return render(request, 'videos/video_list.html', {
			'video_list': video_list,
		})
	# return HttpResponse('This is the video list view.')

def get_video(request, video_id):
	'''
	This view returns a single video.
	'''
	video = Video.objects.get(pk=video_id)

	return render(request, 'videos/video_detail.html', {
			'video': video,
		})
	# return HttpResponse('This is the single video view.')

def post_video(request):
	'''
	Adds a single video to the video list. Post data should be JSON and the only required field is the video URL.
	'''

	return HttpResponse('This is the video post view.')

def delete_video(request, video_id):
	'''
	Deletes a single video from the video list.
	'''

	return HttpResponse('This is the video delete view.')