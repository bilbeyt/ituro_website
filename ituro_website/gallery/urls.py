from django.conf.urls import url
from gallery.views import GalleryDetailView


urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', GalleryDetailView.as_view(),
        name="gallery_detail"),
]
