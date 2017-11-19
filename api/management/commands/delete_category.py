from django.core.management import BaseCommand
import json

from api.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category = Category.objects.all()
        for c in category:
            c.delete()
