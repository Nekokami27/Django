from django.db import models
from django.conf import settings

class TextMessage(models.Model):
	talker =models.CharField(max_length=20, blank=False, default="anything")
	comment = models.CharField(max_length=50, blank=True, default="anything")
	def __str__(self) :
		return self.talker + " " + self.comment

# Create your models here.
