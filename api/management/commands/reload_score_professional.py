from django.core.management import BaseCommand
import json

from api.models import Professional


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Select all professionals
        professionals = Professional.objects.all()

        for pro in professionals:
            # Select all opinions
            opinions = pro.prof_opinion.all()
            scoreTotal = 0

            for opinion in opinions:
                scoreTotal += opinion.score

            try:
            	scoreTotal = scoreTotal / opinions.count()
            except ZeroDivisionError:
            	scoreTotal = 0
            # print (scoreTotal)
            pro.scoreTotal = scoreTotal
            pro.save()
