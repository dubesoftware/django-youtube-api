from django.shortcuts import render, HttpResponse

from videos.models import Video

def index(request):
	'''
	Returns the index page.
	'''

	return HttpResponse('This is the index view.')