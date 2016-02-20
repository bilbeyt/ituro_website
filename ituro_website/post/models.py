from __future__ import unicode_literals
from django.conf import settings
from gallery.models import Gallery,Photo
from ckeditor.fields import RichTextField
from django.contrib.sitemaps import ping_google
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse
from django.contrib.redirects.models import Redirect
from django.db import models


def get_upload_path(instance,filename):
    return "documents/{}/{}".format(instance.title,filename)


class CommonEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    old_slug = models.SlugField(max_length=100)
    slug = models.SlugField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_public = models.BooleanField(default=False)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:common_detail",args=(self.slug,))

class NewsEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=190)
    slug = models.SlugField(max_length=100)
    old_slug = models.SlugField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    types = models.CharField(choices=settings.NEWS_TYPES, max_length=50)
    img = models.ForeignKey(Photo)
    content = RichTextField()
    url_content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:news_detail",args=(self.slug,))


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
    old_slug = models.SlugField(max_length=100)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:category_detail",args=(self.slug,))


class AboutEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_divided = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    content = RichTextUploadingField()
    old_slug = models.SlugField(max_length=100)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:about_detail",args=(self.slug,))


class SponsorshipEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_divided = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    content = RichTextUploadingField()
    old_slug = models.SlugField(max_length=100)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:sponsorship_detail",args=(self.slug,))


class HomePageEntry(models.Model):
    language_code = models.CharField(choices=settings.LANGUAGES,max_length=2)
    title = models.CharField(max_length=50)
    uid = models.PositiveSmallIntegerField()
    content = RichTextField(null=True,blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

@receiver(pre_save,sender=NewsEntry)
def NewsEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.old_slug = instance.slug
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=CommonEntry)
def CommonEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.old_slug = instance.slug
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=CategoryEntry)
def CategoryEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.old_slug = instance.slug
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=AboutEntry)
def AboutEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.old_slug = instance.slug
    instance.slug = slugify(instance.title)

@receiver(pre_save,sender=SponsorshipEntry)
def SponsorshipEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.old_slug = instance.slug
    instance.slug = slugify(instance.title)

@receiver(post_save,sender=CommonEntry,dispatch_uid="commonentry_identifier")
def CommonEntry_slug_change_handler(sender,instance,created,**kwargs):
    try:
        ping_google()
    except Exception:
        pass
    if not created:
        old_link = reverse("post:common_detail",args=(instance.old_slug,))
        new_link=reverse("post:common_detail",args=(instance.slug,))
        Redirect.objects.create(site_id=1,old_path=old_link,new_path=new_link)

@receiver(post_save,sender=CategoryEntry,dispatch_uid="categoryentry_identifier")
def CategoryEntry_slug_change_handler(sender,instance,created,**kwargs):
    try:
        ping_google()
    except Exception:
        pass
    if not created:
        old_link = reverse("post:category_detail",args=(instance.old_slug,))
        new_link=reverse("post:category_detail",args=(instance.slug,))
        Redirect.objects.create(site_id=1,old_path=old_link,new_path=new_link)

@receiver(post_save,sender=AboutEntry,dispatch_uid="aboutentry_identifier")
def AboutEntry_slug_change_handler(sender,instance,created,**kwargs):
    try:
        ping_google()
    except Exception:
        pass
    if not created:
        old_link = reverse("post:about_detail",args=(instance.old_slug,))
        new_link=reverse("post:about_detail",args=(instance.slug,))
        Redirect.objects.create(site_id=1,old_path=old_link,new_path=new_link)

@receiver(post_save,sender=SponsorshipEntry,dispatch_uid="sponsorship_identifier")
def SponsorshipEntry_slug_change_handler(sender,instance,created,**kwargs):
    try:
        ping_google()
    except Exception:
        pass
    if not created:
        old_link = reverse("post:sponsorship_detail",args=(instance.old_slug,))
        new_link=reverse("post:sponsorship_detail",args=(instance.slug,))
        Redirect.objects.create(site_id=1,old_path=old_link,new_path=new_link)
