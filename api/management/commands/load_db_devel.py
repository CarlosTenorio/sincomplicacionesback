from django.core.management import BaseCommand
import json
import random, string

from string import ascii_uppercase
from datetime import datetime
from datetime import date

from django.contrib.auth.models import User

from api.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        def insert_countries():
            print("Deleting countries...")
            Country.objects.all().delete()

            print("Inserting countries...")
            c = Country()
            c.name = "España"
            c.save()

        def insert_provinces():
            print("Deleting provinces...")
            Province.objects.all().delete()

            print("Inserting provinces...")
            with open('data/locationsProvince.json', 'r') as f:
                location_str = f.read()
                locations = json.loads(location_str)

            for location in locations:
                p = Province()
                p.id = location.get('id')
                p.lat = location.get('lat')
                p.lng = location.get('lng')
                p.name = location.get('name')

                name_country = location.get('country')
                country = Country.objects.get(name=name_country)
                p.country = country
                p.save()


        def insert_cities():
            print("Deleting cities...")
            City.objects.all().delete()

            print("Inserting cities...")
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



        def insert_categories():
            print("Deleting categories...")
            Category.objects.all().delete()

            print("Inserting categories...")
            with open('data/categories.json', 'r') as f:
                category_str = f.read()
                categories = json.loads(category_str)


            for category in categories:
                c = Category()
                c.title = category.get('title_es')
                c.description = category.get('description')
                c.save()


        def insert_professionals():
            print("Deleting users and professionals...")
            User.objects.filter().delete()

            print("Creting superuser default...")
            # Create superuser default
            User.objects.create_superuser(username='root', password='Admin1234', email='')
            User.objects.create_superuser(username='admin', password='Admin1234', email='')
            Professional.objects.all().delete()

            print("Inserting users and professionals...")
            # Get all cities
            cities = City.objects.all()
            for idx,i in enumerate(range(1, 500)):

                # Create User Django
                username = "professional" + str(idx)
                email = username + "@mail.com"
                password = "User1234"
                user_django = User.objects.create_user(username=email, password=password)
                user_django.email = email
                user_django.save()

                # Create Professional Model
                pro = Professional()
                pro.user = user_django
                pro.username = username
                pro.web_prof = ''.join(random.choice(ascii_uppercase) for i in range(6))
                pro.adress_prof = ''.join(random.choice(ascii_uppercase) for i in range(6))
                pro.scoreTotal = random.randint(0, 5)
                pro.city = random.choice(cities)

                pro.save()


        def insert_my_users():
            print("Deleting my users...")
            # No need to delete User class because they have already been deleted when inserting the professionals
            MyUser.objects.all().delete()

            print("Inserting users and my users...")
            # Get all cities
            cities = City.objects.all()
            # Create my users
            for idx,i in enumerate(range(1, 25)):
                # Create User Django
                username = "myuser" + str(idx)
                email = username + "@mail.com"
                password = "User1234"
                user_django = User.objects.create_user(username=email, password=password)
                user_django.email = email
                user_django.save()

                my_user = MyUser()
                my_user.user = user_django
                my_user.username = username
                my_user.city = random.choice(cities)

                my_user.save()


        def insert_professionals_profile():
            print("Deleting professionals profiles...")
            ProfessionalProfile.objects.all().delete()

            print("Inserting professionals profiles...")
            professionals = Professional.objects.all()
            for pro in professionals:

                # Create Professional Model
                proProf = ProfessionalProfile()
                proProf.professional = pro

                img_url_1 = '../static/img/user-profile.jpg'
                img_url_2 = '../static/img/user-cover.jpg'

                proProf.profile_photo = img_url_1
                proProf.profile_cover = img_url_2

                proProf.save()


        def insert_my_users_profile():
            print("Deleting my users profiles...")
            MyUserProfile.objects.all().delete()

            print("Inserting my users profiles...")
            mu_users = MyUser.objects.all()
            for my_us_x in mu_users:

                # Create Professional Model
                my_user_Prof = MyUserProfile()
                my_user_Prof.myUser = my_us_x

                img_url_1 = '../static/img/user-profile.jpg'
                img_url_2 = '../static/img/user-cover.jpg'

                my_user_Prof.profile_photo = img_url_1
                my_user_Prof.profile_cover = img_url_2

                my_user_Prof.save()


        def insert_professionals_folders():
            print("Deleting professionals folders...")
            ProfessionalFolder.objects.all().delete()

            print("Inserting professionals folders...")
            professionals = Professional.objects.all()

            for pro in professionals:
                # Create [1-4] professional folders
                for idx,i in enumerate(range(1, random.randint(2, 5))):
                # Create Professional Folder
                    professionals_folders = ProfessionalFolder()
                    professionals_folders.title = "Otros" + str(idx)
                    professionals_folders.description = "Lorem ipsum"
                    professionals_folders.professional = pro
                    professionals_folders.save()


        def insert_professionals_tatto_photos():
            print("Deleting professionals tattoo photos ...")
            TattooPhoto.objects.all().delete()

            print("Inserting professionals tattoo photos..")
            # Get all professional folders of tattoos
            professionals_folders = ProfessionalFolder.objects.all()

            for pro_folder in professionals_folders:
                # Create [1-20] professional tattoo photos
                for idx,i in enumerate(range(1, random.randint(2, 20))):
                    # Create new professional tattoo photo
                    tattoo_photo = TattooPhoto()

                    img_url_tattoo = '../static/img/user-profile.jpg'

                    tattoo_photo.image = img_url_tattoo
                    tattoo_photo.professional_folder = pro_folder
                    # Select one category random
                    # categories = Category.objects.all()
                    # tattoo_photo.category.add(random.choice(categories))

                    tattoo_photo.save()


        def insert_opinions():
            print("Deleting opinions...")
            Opinion.objects.all().delete()

            print("Inserting opinions...")
            # Get all the professionals
            professionals = Professional.objects.all()
            # Get all my users
            my_users = MyUser.objects.all()

            for pro in professionals:
                # Create [1-4] opinions
                for idx,i in enumerate(range(1, random.randint(2, 10))):
                # Create Opinion
                    op = Opinion()
                    op.title = "Lorem ipsum" + str(idx)
                    op.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris odio nisl, sagittis in sollicitudin sit amet, rhoncus at mi. Donec"

                    # Create [1-5] score
                    op.score = random.randint(1, 6)

                    # Select one MyUser random
                    op.user = random.choice(my_users)

                    op.professional = pro
                    op.save()


        def insert_comments():
            print("Deleting comments...")
            Comment.objects.all().delete()

            print("Inserting comments...")
            # Get all opinions
            opinions = Opinion.objects.all()
            # Get all my users
            my_users = MyUser.objects.all()
            # Get all the professionals
            professionals = Professional.objects.all()

            for opi in opinions:
                # Create [1-10] comments
                for idx,i in enumerate(range(1, random.randint(2, 10))):
                    # Create Commnet
                    cm = Comment()
                    cm.body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris"

                    # Select one MyUser random
                    cm.myUser = random.choice(my_users)

                    # Select one Professional random
                    cm.prof = random.choice(professionals)

                    cm.opinion = opi
                    cm.save()


        def insert_usefuls_opinion():
            print("Deleting usefuls opinion...")
            UsefulOpinion.objects.all().delete()

            print("Inserting usefuls opinion...")
            # Get all opinions
            opinions = Opinion.objects.all()
            # Get all my users
            my_users = MyUser.objects.all()

            for opi in opinions:
                # Create [1-10] usefuls opinion
                for idx,i in enumerate(range(1, random.randint(2, 10))):
                    # Create Commnet
                    us_op = UsefulOpinion()

                    # Select one MyUser random
                    us_op.myUser = random.choice(my_users)

                    us_op.opinion = opi
                    us_op.save()


        def insert_usefuls_comments():
            print("Deleting usefuls comment...")
            UsefulComment.objects.all().delete()

            print("Inserting usefuls comment...")
            # Get all comments
            comments = Comment.objects.all()
            # Get all my users
            my_users = MyUser.objects.all()

            for cm in comments:
                # Create [1-10] usefuls comment
                for idx,i in enumerate(range(1, random.randint(2, 10))):
                    # Create Commnet
                    us_cm = UsefulComment()
                    # Select one MyUser random
                    us_cm.user = random.choice(my_users)
                    us_cm.comment = cm

                    cm.save()


        ########################################################
        # Insert all data
        ########################################################
        insert_countries()
        print ()
        insert_provinces()
        print ()
        insert_cities()
        print ()
        insert_categories()
        print ()
        insert_professionals()
        print ()
        insert_my_users()
        print ()
        insert_professionals_profile()
        print ()
        insert_my_users_profile()
        print ()
        insert_professionals_folders()
        print()
        insert_professionals_tatto_photos()
        print ()
        insert_opinions()
        print ()
        insert_comments()
        print ()
        insert_usefuls_opinion()
        print ()
        insert_usefuls_comments()
        print ()
        print ("Insert data successful")
