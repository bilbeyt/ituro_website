from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import get_language
from django.utils.translation import activate
from post.models import CommonEntry
from post.models import NewsEntry
from post.models import CategoryEntry
from post.models import HomePageEntry
from post.models import AboutEntry
from post.models import SponsorshipEntry


class HomePageDetailView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        language_code = self.request.LANGUAGE_CODE
        news_list = NewsEntry.objects.filter(language_code=language_code)
        homepage = HomePageEntry.objects.get(language_code=language_code)
        context = super(HomePageDetailView,self).get_context_data(**kwargs)
        context["homepage"] = homepage
        context["news_list"] = news_list
	context["countdown_time"] = homepage.countdown_time.isoformat()
        return context


class NewsEntryDetailView(DetailView):
    model = NewsEntry
    template_name = "news_detail.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        uid = self.object.uid
        language = request.LANGUAGE_CODE
        new_obj = NewsEntry.objects.get(uid=uid,language_code=language)
        slug = self.kwargs.get("slug")
        if slug != new_obj.slug:
            return HttpResponseRedirect(reverse("post:news_detail",args=(new_obj.slug,)))
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class CategoryDetailView(DetailView):
    model = CategoryEntry
    template_name = "category_detail.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        uid = self.object.uid
        language = request.LANGUAGE_CODE
        new_obj = CategoryEntry.objects.get(uid=uid,language_code=language)
        slug = self.kwargs.get("slug")
        if slug != new_obj.slug:
            return HttpResponseRedirect(reverse("post:category_detail",args=(new_obj.slug,)))
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class CommonDetailView(DetailView):
    model = CommonEntry
    template_name = "commonentry_detail.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        uid = self.object.uid
        language = request.LANGUAGE_CODE
        new_obj = CommonEntry.objects.get(uid=uid,language_code=language)
        slug = self.kwargs.get("slug")
        if slug != new_obj.slug:
            return HttpResponseRedirect(reverse("post:common_detail",args=(new_obj.slug,)))
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class AboutDetailView(DetailView):

    model = AboutEntry
    template_name = "about_detail.html"

    def get(self, request, **kwargs):
    
        self.object = self.get_object()
        uid = self.object.uid
        language = get_language()
        new_obj = AboutEntry.objects.get(uid=uid,language_code=language)
        slug = self.kwargs.get("slug")
        if slug != new_obj.slug:
            return HttpResponseRedirect(reverse("post:about_detail",args=(new_obj.slug,)))
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class SponsorshipDetailView(DetailView):
    model = SponsorshipEntry
    template_name = "sponsorship_detail.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        uid = self.object.uid
        language = request.LANGUAGE_CODE
        new_obj = SponsorshipEntry.objects.get(uid=uid,language_code=language)
        slug = self.kwargs.get("slug")
        if slug != new_obj.slug:
            return HttpResponseRedirect(reverse("post:sponsorship_detail",args=(new_obj.slug,)))
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
