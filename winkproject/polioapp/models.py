from django.db import models

# Create your models here.

#blog-> project-----------
class Pblog(models.Model): 
    p_boardname = models.CharField(default="Project",max_length=200)
    p_title = models.CharField(max_length=200)
    p_pub_date = models.DateTimeField('date published')
    p_body = models.TextField()

    def __str__(self):
        return self.p_title

    def p_summary(self):
        return self.p_body[:100]

#News-> News-----------
class Nblog(models.Model): 
    p_boardname = models.CharField(default="News",max_length=200)
    n_title = models.CharField(max_length=200)
    n_pub_date = models.DateTimeField('date published')
    n_body = models.TextField()

    def __str__(self):
        return self.n_title

    def n_summary(self):
        return self.n_body[:100]