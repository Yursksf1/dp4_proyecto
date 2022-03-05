from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('001', views.index2, name='chiste_1'),
    path('002', views.index3, name='chiste_2'),
]