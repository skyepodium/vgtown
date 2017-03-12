from django.db import models
from django.conf import settings

class BannerModel(models.Model):

	reg_time = models.DateTimeField(auto_now_add=True, null=False)
	title = models.CharField(max_length=255, null=False)
	link_url = models.CharField(max_length=255, null=True, blank=True)
	image = models.ImageField(upload_to = "images/", blank=True, null=True)
	order_no = models.IntegerField(null=True)
	color = models.CharField(max_length=20, null=True, blank=True)
