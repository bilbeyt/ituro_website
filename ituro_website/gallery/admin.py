from django.contrib import admin
from gallery.models import Gallery,Photo


class PhotoInlineAdmin(admin.TabularInline):
    model = Photo
    extra = 0
    exclude = ["thumbnail"]
    readonly_fields = ("preview",)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "language_code", "preview","uid","created_at"]
    list_filter = ["language_code"]
    search_fields = ["uid", "title"]
    exclude = ["gallery", "thumbnail"]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ["title", "old_slug","slug","language_code", "order","uid","created_at"]
    list_filter = ["language_code"]
    search_fields = ["uid", "title"]
    exclude = ["old_slug","slug"]
    inlines = [PhotoInlineAdmin]


admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Photo,PhotoAdmin)
