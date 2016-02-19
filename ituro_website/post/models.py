from __future__ import unicode_literals
from django.conf import settings
from gallery.models import Gallery,Photo
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


def get_upload_path(instance,filename):
    return "documents/{}/{}".format(instance.title,filename)


class CommonEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_public = models.BooleanField(default=False)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class NewsEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=190)
    slug = models.SlugField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    types = models.CharField(choices=settings.NEWS_TYPES, max_length=50)
    img = models.ForeignKey(Photo)
    content = RichTextField()
    url_content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class CategoryEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_divided = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    document = models.FileField(upload_to=get_upload_path)
    gallery = models.ForeignKey(Gallery)
    url = models.URLField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title


class AboutEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_divided = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title


class SponsorshipEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_divided = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title


class HomePageEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=50)
    uid = models.PositiveSmallIntegerField()
    content = RichTextField(null=True,blank=True)
    url = models.URLField()
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


@receiver(pre_save,sender=NewsEntry)
def NewsEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=CommonEntry)
def CommonEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=CategoryEntry)
def CategoryEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=AboutEntry)
def AboutEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=SponsorshipEntry)
def SponsorshipEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=HomePageEntry)
def HomePageEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)
