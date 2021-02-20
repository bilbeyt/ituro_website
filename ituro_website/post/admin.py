from django.contrib import admin
from post.models import CommonEntry, NewsEntry, CategoryEntry, HomePageEntry, \
    AboutEntry, SponsorshipEntry, Category3DModel,Seminar


class Category3DModelAdmin(admin.TabularInline):
    model = Category3DModel
    extra = 1


class CommonEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "old_slug","slug","language_code","order","uid","created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["old_slug","slug"]


class HomePageEntryAdmin(admin.ModelAdmin):
    list_display = ["title","language_code","url","uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]


class AboutEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "old_slug","slug","language_code","order", "uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["old_slug","slug"]


class SponsorshipEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "old_slug","slug","language_code","order", "uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["old_slug","slug"]


class CategoryEntryAdmin(admin.ModelAdmin):
    inlines = [Category3DModelAdmin]
    list_display = ["title", "old_slug","slug","language_code", "gallery", "url","order", "uid",
        "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude =["old_slug","slug"]


class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "old_slug","slug","language_code", "types", "uid", "created_at"]
    list_filter = ["language_code"]
    search_fields = ["title","uid"]
    exclude = ["old_slug","slug"]




admin.site.register(CommonEntry,CommonEntryAdmin)
admin.site.register(CategoryEntry,CategoryEntryAdmin)
admin.site.register(NewsEntry,NewsEntryAdmin)
admin.site.register(SponsorshipEntry,SponsorshipEntryAdmin)
admin.site.register(AboutEntry,AboutEntryAdmin)
admin.site.register(HomePageEntry,HomePageEntryAdmin)
admin.site.register(Seminar)
