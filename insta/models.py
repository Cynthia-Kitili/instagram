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

    def delete_pic(self):
    	self.delete()

    def save_pic(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.pic_caption = new_caption
    	self.save()   

    @classmethod
    def get_pics_by_user(cls,id):
        sent_pics = Pic.objects.filter(user_id=id)
        return sent_pics

    @classmethod
    def get_pics_by_id(cls,id):
        fetched_pic = Pic.objects.get(id = id)
        return  fetched_pic

    class Meta:
    	ordering = ['-pub_date']


    def __str__(self):
    	return self.user.username

    def save_profile(self):
    	self.save()     