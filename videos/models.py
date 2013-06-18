from django.db import models

class Video(models.Model):	
	video_title = models.CharField(max_length=250, blank=True)
	video_description = models.TextField(max_length=1000, blank=True)
	video_link = models.URLField()

	def __unicode__(self):
		if self.video_title is not None:
			return self.video_title
		else:
			return self.video_link