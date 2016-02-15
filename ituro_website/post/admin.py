from django.contrib import admin
from post.models import CommonEntry, NewsEntry, CategoryEntry, HomePageEntry, \
    AboutEntry, SponsorshipEntry


class CommonEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","language_code","order","uid","created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["slug"]


class HomePageEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","language_code","url","uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["slug"]


class AboutEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","language_code","order", "uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["slug"]


class SponsorshipEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","language_code","order", "uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["slug"]


class CategoryEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","language_code", "gallery", "url","order", "uid",
        "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["slug"]


class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","language_code", "types", "uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude = ["slug"]


admin.site.register(CommonEntry,CommonEntryAdmin)
admin.site.register(CategoryEntry,CategoryEntryAdmin)
admin.site.register(NewsEntry,NewsEntryAdmin)
admin.site.register(SponsorshipEntry,SponsorshipEntryAdmin)
admin.site.register(AboutEntry,AboutEntryAdmin)
admin.site.register(HomePageEntry,HomePageEntryAdmin)
