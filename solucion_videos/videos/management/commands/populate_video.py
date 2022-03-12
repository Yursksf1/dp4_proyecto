# Django
from django.core.management.base import BaseCommand

# Models
from videos.models import Video


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("vamos a hacer un populate es decir llenar la data de la tabla video")
        import pandas as pd

        path = r'C:\Users\yajhaira.sanchez\proyectos_yurley\dp4_proyecto\solucion_videos\videos\management\commands\import.xlsx'
        df = pd.read_excel(path)
        print("show df")
        print(df)

        
        video_data = ['nombre del video', 'descripcion del video', 'www.youtube.com']
        video = Video()
        video.title = video_data[0]
        video.description = video_data[1]
        video.link = video_data[2]
        video.save()