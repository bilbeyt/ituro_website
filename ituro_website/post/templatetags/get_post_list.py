from post.models import AboutEntry, CommonEntry, CategoryEntry, SponsorshipEntry
from django import template


register = template.Library()


@register.assignment_tag
def get_post_list(language_code):
    context = dict()
    context["about_list"] = AboutEntry.objects.filter(language_code=language_code, is_public=True)
    context["category_list"] = CategoryEntry.objects.filter(language_code=language_code, is_public=True)
    context["sponsorship_list"] = SponsorshipEntry.objects.filter(language_code=language_code, is_public=True)
    context["common_list"] = CommonEntry.objects.filter(language_code=language_code, is_public=True)
    return context
