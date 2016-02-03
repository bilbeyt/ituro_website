from __future__ import unicode_literals
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from gallery.models import Gallery
from django.db import models


def get_image_upload_path(instance,filename):
    return "news/{}/{}".format(instance.title,filename)

def get_file_upload_path(instance,filename):
    return "documents/{}/{}".format(instance.category,filename)


class NewsEntry(models.Model):
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    category = models.CharField(choices=settings.NEWS_CATEGORIES, max_length=50)
    title = models.CharField(max_length=100)
    content = RichTextField()
    img = models.ImageField(upload_to=get_image_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.title


class CategoryEntry(models.Model):
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    category = models.CharField(max_length=100, choices=settings.CATEGORIES)
    document = models.FileField(upload_to=get_file_upload_path)
    gallery = models.ForeignKey(Gallery)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class CommonEntry(models.Model):
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    page = models.CharField(choices=settings.PAGES, max_length=50)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Link(models.Model):
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    page = models.CharField(choices=settings.PAGES, max_length=100)
    entry = models.ForeignKey(CommonEntry)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


@receiver(pre_save,sender=NewsEntry)
def NewsEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)
