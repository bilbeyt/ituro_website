from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from gallery.models import Gallery,Photo


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = "gallery_detail.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        uid = self.object.uid
        language = request.LANGUAGE_CODE
        new_obj = Gallery.objects.get(uid=uid,language_code=language)
        slug = self.kwargs.get("slug")
        if slug != new_obj.slug:
            return HttpResponseRedirect(reverse("gallery:gallery_detail",args=(new_obj.slug,)))
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
