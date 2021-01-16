from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Pic(models.Model):
    pic = models.ImageField(upload_to = "pics/",null = True)
    user = models.ForeignKey(User,null=True)
    pic_name = models.CharField(max_length = 30,null = True)
    likes = models.IntegerField(default=0)
    pic_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    # profile = models.ForeignKey(Profile, null=True) 
    comments = models.IntegerField(default=0)


    def __str__(self):
    	return self.pic_name