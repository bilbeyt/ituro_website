from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class Gallery(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES, max_length=2)
    title = models.CharField(max_length=50, choices=settings.GALLERY_PAGES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


def get_upload_path(instance,filename):
    return "gallery/{}/{}".format(instance.gallery,filename)


class Photo(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES, max_length=2)
    gallery = models.ForeignKey(Gallery)
    description = models.CharField(max_length=50)
    img = models.ImageField(upload_to=get_upload_path)
    is_thumbnail = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description
