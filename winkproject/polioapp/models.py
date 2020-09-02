from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

#blog-> project-----------
class Pblog(models.Model): 
    p_boardname = models.CharField(default="Project",max_length=200)
    p_title = models.CharField(max_length=200)
    p_pub_date = models.DateTimeField('date published')
    p_body = models.TextField()
    p_images = models.ImageField(blank=True, upload_to="p_images", null=True)
    p_link = models.TextField(null=True )
    p_writer = models.CharField(max_length=50, default="by윤정")
    p_views=models.PositiveIntegerField(default=0) #조회수
    

    def __str__(self):
        return self.p_title

    def p_summary(self):
        return self.p_body[:100]
    
    @property
    def update_pcounter(self):
        self.p_views = self.p_views + 1
        self.save()

#News-> News-----------
class Nblog(models.Model): 
    p_boardname = models.CharField(default="News",max_length=200)
    n_title = models.CharField(max_length=200)
    n_pub_date = models.DateTimeField('date published')
    n_body = models.TextField()
    n_images = models.ImageField(blank=True, upload_to="n_images", null=True)
    n_writer = models.CharField(max_length=50, default="by윤정")
    n_views=models.PositiveIntegerField(default=0) #조회수

    def __str__(self):
        return self.n_title

    def n_summary(self):
        return self.n_body[:100]
    
    @property
    def update_ncounter(self):
        self.n_views = self.n_views + 1
        self.save()