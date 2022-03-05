from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('install', views.install, name='install'),
    path('models', views.models, name='models'),
    path('002', views.index3, name='chiste_2'),
]