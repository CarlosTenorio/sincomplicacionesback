from django.core.management import BaseCommand
import json

from api.models import City


class Command(BaseCommand):

    def handle(self, *args, **options):

        city = City.objects.all()
        for c in city:
            c.delete()