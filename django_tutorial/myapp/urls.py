from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('install', views.install, name='install'),
    path('archivos/models', views.models, name='models'),
    path('archivos/urls', views.urls, name='urls'),
    path('archivos/views', views.views, name='views'),
    path('archivos/templates', views.templates, name='templates'),
]