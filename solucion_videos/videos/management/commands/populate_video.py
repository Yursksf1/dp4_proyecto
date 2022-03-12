# Django
from django.core.management.base import BaseCommand

# Models
from videos.models import Video


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("vamos a hacer un populate es decir llenar la data de la tabla video")
