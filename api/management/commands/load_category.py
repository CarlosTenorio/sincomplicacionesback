from django.core.management import BaseCommand
import json

from api.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data/categories.json', 'r') as f:
            category_str = f.read()
            categories = json.loads(category_str)


        for category in categories:
            c = Category()
            c.title = category.get('title_es')
            c.description = category.get('description')
            c.save()
