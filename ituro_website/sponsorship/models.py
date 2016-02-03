from __future__ import unicode_literals
from pages.models import Link
from django.conf import settings
from django.db import models


def get_upload_path(instance,filename):
    return "sponsors/{}/{}".format(instance.name,filename)


class Sponsor(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    sponsor_type = models.CharField(choices=settings.SPONSOR_TYPES,max_length=50)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to=get_upload_path)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
