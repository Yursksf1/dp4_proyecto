# Django
from django.core.management.base import BaseCommand

# Models
from videos.models import Video
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("vamos a hacer un populate es decir llenar la data de la tabla video")
        path = r'C:\Users\yajhaira.sanchez\proyectos_yurley\dp4_proyecto\solucion_videos\videos\management\commands\import.xlsx'
        df = pd.read_excel(path)
        print("show df")
        print(df)
        
        for index, row in df.iterrows():
            print("creando registro.")
            video = Video()
            video.title = row["titulo"]
            video.description = row["descripcion"]
            video.link = row["link"]
            video.save()

        print("fin")