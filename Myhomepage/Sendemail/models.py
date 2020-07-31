from django.db import models
from Myinfo.models import Myinfo

class Sendemail(models.Model):
	email = models.CharField(max_length=30, default="jje0ng@kookmin.ac.kr")
	Outemail = models.CharField(max_length=100)
	content = models.CharField(max_length=1000)
