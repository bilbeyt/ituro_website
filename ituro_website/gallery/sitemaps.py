from django.contrib.sitemaps import Sitemap
from django.utils.translation import get_language
from gallery.models import Gallery


class GallerySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Gallery.objects.filter(language_code=get_language(),is_public=True)

    def lastmod(self, obj):
        return obj.created_at
