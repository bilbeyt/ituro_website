from django.contrib.sitemaps import Sitemap
from django.utils.translation import get_language
from post.models import CommonEntry,NewsEntry,AboutEntry,SponsorshipEntry, CategoryEntry


class CommonEntrySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return CommonEntry.objects.filter(language_code=get_language(),is_public=True)

    def lastmod(self, obj):
        return obj.created_at


class NewsEntrySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return NewsEntry.objects.filter(language_code=get_language())

    def lastmod(self, obj):
        return obj.created_at


class CategoryEntrySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return CategoryEntry.objects.filter(language_code=get_language(),is_public=True)

    def lastmod(self, obj):
        return obj.created_at


class AboutEntrySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return AboutEntry.objects.filter(language_code=get_language(),is_public=True)

    def lastmod(self, obj):
        return obj.created_at


class SponsorshipEntrySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return SponsorshipEntry.objects.filter(language_code=get_language(),is_public=True)

    def lastmod(self, obj):
        return obj.created_at
