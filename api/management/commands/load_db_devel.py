from django.core.management import BaseCommand
import json
import random, string

from string import ascii_uppercase
from datetime import datetime
from datetime import date

from django.contrib.auth.models import User

from api.models import Country, Expansion


class Command(BaseCommand):

    def handle(self, *args, **options):

        def insert_countries():
            print("Deleting countries...")
            Country.objects.all().delete()

            print("Inserting countries...")
            c = Country()
            c.name = "España"
            c.save()

        def insert_users():
            print("Deleting my users...")
            # No need to delete User class because they have already been
            # deleted when inserting the professionals
            User.objects.all().delete()

            print("Inserting users...")
            # Create my users
            for idx, i in enumerate(range(1, 25)):
                # Create User Django
                username = "useTest" + str(idx)
                email = username + "@mail.com"
                password = "User1234"
                user_django = User.objects.create_user(username=email, password=password)
                user_django.email = email
                user_django.save()

        def insert_expansions():
            print("Deleting expansions...")
            Expansion.objects.all().delete()

            print("Inserting expansions...")
            with open('data/expansions.json', 'r') as f:
                expansion_str = f.read()
                expansions = json.loads(expansion_str)

            for expansion in expansions:
                e = Expansion()
                e.title = expansion.get('title')
                e.save()


        ########################################################
        # Insert all data
        ########################################################
        insert_countries()
        print()
        insert_users()
        print()
        insert_expansions()
        print("Insert data successful")
