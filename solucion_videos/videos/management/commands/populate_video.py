# Django
from django.core.management.base import BaseCommand

# Models
from videos.models import Video


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("vamos a hacer un populate es decir llenar la data de la tabla video")
        video_data = ['nombre del video', 'descripcion del video', 'www.youtube.com']
        video = Video()
        video.title = video_data[0]
        video.description = video_data[1]
        video.link = video_data[2]
        video.save()