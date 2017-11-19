from django.core.management import BaseCommand
from api.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        c = Country()
        c.name = "España"
        c.save()
