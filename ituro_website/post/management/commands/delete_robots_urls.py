from django.core.management import BaseCommand
from robots.models import Url


class Command(BaseCommand):
    help = 'Deletes urls for robots.txt'

    def handle(self,*args,**kwargs):

        for url in Url.objects.all():
            url.delete()

        self.stdout.write('Urls deleted')
