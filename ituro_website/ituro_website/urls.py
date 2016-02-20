from django.conf.urls import url,include
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from gallery.sitemaps import GallerySitemap
from post.sitemaps import AboutEntrySitemap,CategoryEntrySitemap,CommonEntrySitemap, \
    NewsEntrySitemap,SponsorshipEntrySitemap


sitemaps = {
    'news' : NewsEntrySitemap,
    'about' : AboutEntrySitemap,
    'category' : CategoryEntrySitemap,
    'sponsorship' : SponsorshipEntrySitemap,
    'gallery' : GallerySitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include("ckeditor_uploader.urls")),
    url(r'^robots\.txt', include('robots.urls')),
]

urlpatterns += i18n_patterns(

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(_(r'^gallery/'), include("gallery.urls",namespace="gallery")),
    url(r'^', include("post.urls", namespace="post")),


)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
