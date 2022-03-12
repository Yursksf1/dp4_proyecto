from django.shortcuts import render, redirect
from .models import Video

# Create your views here.

def index(request):
    videos = Video.objects.all()
    print('videos', videos)
    print("cantidad de videos: ", len(videos))
    return render(request, 'videos/index.html', {
        "cantidad": len(videos),
        "videos": videos
    })

def video_detail(request, id):
    pass
