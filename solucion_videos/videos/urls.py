from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_detail/<id>', views.video_detail, name='detail')
]