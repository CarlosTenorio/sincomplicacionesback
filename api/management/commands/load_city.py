from django.core.management import BaseCommand
import json

from api.models import City
from api.models import Province
from api.models import PostalCode


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data/locationsMunicipality.json', 'r') as f:
            location_str = f.read()
            locations = json.loads(location_str)


        for location in locations:
            c = City()
            # c.lat = location.get('lat')
            # c.lng = location.get('lng')
            c.name = location.get('name')

            province = Province.objects.get(name=location.get('province'))

            c.province = province

            # Create postal code objects
            # postal = location.get('postal')

            c.save()

            # for locationCode in postal.get('codes'):
            #     cp = PostalCode()
            #     cp.code = int(locationCode.get('code'))
            #     cp.city = c
            #     cp.save()
