from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from post.views import HomePageDetailView, AboutDetailView, \
    CategoryDetailView, SponsorshipDetailView, CommonDetailView, \
    NewsEntryDetailView, contactView, successView


urlpatterns = [

    url(r'^$', HomePageDetailView.as_view(), name="homepage"),
    url(_(r'^contact_us/$'), contactView, name="contact"),
    url(_(r'^success/$'), successView, name="success"),
    url(_(r'^about/(?P<slug>[-_\w]+)/$'), AboutDetailView.as_view(),
        name="about_detail"),
    url(_(r'^category/(?P<slug>[-_\w]+)/$'), CategoryDetailView.as_view(),
        name="category_detail"),
    url(_(r'^sponsorship/(?P<slug>[-_\w]+)/$'), SponsorshipDetailView.as_view(),
        name="sponsorship_detail"),

    url(_(r'^news/(?P<slug>[-_\w]+)/$'), NewsEntryDetailView.as_view(),
        name="news_detail"),
    url(r'^(?P<slug>[-_\w]+)/$', CommonDetailView.as_view(),
        name="common_detail"),
]
