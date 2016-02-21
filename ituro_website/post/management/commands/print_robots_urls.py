from django.core.management import BaseCommand
from robots.models import Url


class Command(BaseCommand):
    help = 'Prints urls for robots.txt'

    def handle(self,*args,**kwargs):

        for url in Url.objects.all():
            self.stdout.write("{}".format(url.pattern))
