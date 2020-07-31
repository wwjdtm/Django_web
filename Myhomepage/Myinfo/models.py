from django.db import models

# Create your models here.

class Myinfo(models.Model):
	name = models.CharField(max_length=30, default="김윤정")
	photo = models.CharField(max_length=500, null=True, blank=True)
	email = models.CharField(max_length=100)
	github_link = models.CharField(max_length=100)
	skill = models.CharField(max_length=500)
	sns = models.CharField(max_length=100)
	introduction = models.CharField(max_length=1000)

	def __str__(self):
		return self.name
