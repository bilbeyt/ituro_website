from gallery.models import Gallery
from django import template


register = template.Library()


@register.assignment_tag
def get_gallery_list(language_code):
    gallery_list = Gallery.objects.filter(language_code=language_code, is_public=True)
    return gallery_list
