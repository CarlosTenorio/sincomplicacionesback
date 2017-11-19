from django.core.management import BaseCommand
import json

from api.models import Province


class Command(BaseCommand):

    def handle(self, *args, **options):

        province = Province.objects.all()
        for p in province:
            p.delete()