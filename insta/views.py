from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import ProfileUploadForm,CommentForm,ProfileForm
from django.http  import HttpResponse
from . models import Pic ,Profile, Likes, Follow, Comment,Unfollow
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
      title = 'Instagram'
      pic_posts = Pic.objects.all()
      # comments = Comment.objects.all()

      print(pic_posts)
      return render(request, 'index.html', {"title":title,"pic_posts":pic_posts})