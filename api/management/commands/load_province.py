from django.core.management import BaseCommand
import json

from api.models import Province
from api.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data/locationsProvince.json', 'r') as f:
            location_str = f.read()
            locations = json.loads(location_str)

        country = Country.objects.get(name="España")
        for location in locations:
            p = Province()
            p.lat = location.get('lat')
            p.lng = location.get('lng')
            p.name = location.get('name')
            p.country = country
            p.save()
