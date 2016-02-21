from django.core.management import BaseCommand
from post.models import NewsEntry,CommonEntry,CategoryEntry,AboutEntry,SponsorshipEntry
from gallery.models import Gallery
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from robots.models import Url


class Command(BaseCommand):
    help = 'Generates urls for robots.txt'

    def handle(self,*args,**kwargs):

        for about in AboutEntry.objects.all():
            language_code = about.language_code
            activate(language_code)
            url = reverse("post:about_detail",args=(about.slug,))
            Url.objects.create(pattern=url)

        for common in CommonEntry.objects.all():
            language_code = about.language_code
            activate(language_code)
            url = reverse("post:common_detail",args=(common.slug,))
            Url.objects.create(pattern=url)

        for news in NewsEntry.objects.all():
            language_code = about.language_code
            activate(language_code)
            url = reverse("post:news_detail",args=(news.slug,))
            Url.objects.create(pattern=url)

        for category in CategoryEntry.objects.all():
            language_code = about.language_code
            activate(language_code)
            url = reverse("post:category_detail",args=(category.slug,))
            Url.objects.create(pattern=url)

        for sponsorship in SponsorshipEntry.objects.all():
            language_code = about.language_code
            activate(language_code)
            url = reverse("post:sponsorship_detail",args=(sponsorship.slug,))
            Url.objects.create(pattern=url)

        for gallery in Gallery.objects.all():
            language_code = about.language_code
            activate(language_code)
            url = reverse("gallery:gallery_detail",args=(gallery.slug,))
            Url.objects.create(pattern=url)

        self.stdout.write('Urls generated for robots.txt')
