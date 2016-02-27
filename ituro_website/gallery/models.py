from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from django.utils.translation import activate
from django.contrib.redirects.models import Redirect
from django.template.defaultfilters import slugify
from django.contrib.sitemaps import ping_google
from django.dispatch import receiver
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


def get_image_upload_path(instance,filename):
    return "gallery/{}/photos/{}".format(instance.gallery,filename)

def get_thumbnail_upload_path(instance,filename):
    return "gallery/{}/thumbnails/{}".format(instance.gallery,filename)

class Gallery(models.Model):
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    is_divided = models.BooleanField(default=False)
    old_slug = models.SlugField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery:gallery_detail",args=(self.slug,))


class Photo(models.Model):
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    title = models.CharField(max_length=100)
    uid = models.PositiveSmallIntegerField()
    gallery = models.ForeignKey(Gallery)
    img = models.ImageField(upload_to=get_image_upload_path)
    thumbnail = models.ImageField(upload_to=get_thumbnail_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def preview(self):
        return u'<img src="%s" width="80" height="80"/>' % (self.img.url)
    preview.allow_tags = True
    preview.short_description = "Photo"


@receiver(pre_save,sender=Photo)
def photo_thumbnail_handler(sender,instance,*args,**kwargs):
    image = Img.open(StringIO.StringIO(instance.img.read()))
    if image.format == 'tif':
        image = image.convert("RGB")    
    image.thumbnail((100,100), Img.ANTIALIAS)
    output = StringIO.StringIO()
    image.save(output, format='PNG',optimize=True)
    output.seek(0)
    instance.thumbnail= InMemoryUploadedFile(output,'ImageField', "%s.png" %instance.img.name.split(".")[0], 'image/png', output.len, None)

@receiver(pre_save,sender=Gallery)
def Gallery_slug_handler(sender,instance,*args,**kwargs):
    instance.old_slug = instance.slug
    instance.slug = slugify(instance.title)

@receiver(post_save,sender=Gallery,dispatch_uid="gallery_identifier")
def Gallery_slug_change_handler(sender,instance,created,**kwargs):
    if not created:
        language_code = instance.language_code
        activate(language_code)
        old_link = reverse("gallery:gallery_detail",args=(instance.old_slug,))
        new_link=reverse("gallery:gallery_detail",args=(instance.slug,))
        if new_link != old_link:
            Redirect.objects.create(site_id=1,old_path=old_link,new_path=new_link)
            try:
                ping_google()
            except Exception:
                pass
        else:
            pass
