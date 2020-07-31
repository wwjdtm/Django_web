from django.db import models
from Myinfo.models import Myinfo
from datetime import datetime

class Board(models.Model):
	board_num = models.IntegerField()
	board_name = models.CharField(max_length=100)
	board_detail = models.CharField(max_length=300)

	def __str__(self):
		return self.board_name

class Post(models.Model):
	post_num = models.AutoField(primary_key=True)
	board_name = models.ForeignKey(Board, on_delete=models.CASCADE)
	post_name = models.CharField(max_length=100)
	post_detail = models.CharField(max_length=300)
	post_link = models.CharField(max_length=300)
	name = models.ForeignKey(Myinfo, on_delete=models.CASCADE)
	post_write = models.DateTimeField(default=datetime.now)
	post_views = models.IntegerField(default=0)


	def __str__(self):
		return self.post_name
