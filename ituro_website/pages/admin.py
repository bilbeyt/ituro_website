from django.contrib import admin
from pages.models import NewsEntry,CategoryEntry,CommonEntry,Link


class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "language_code", "created_at"]
    list_filter = ["category"]
    search_fields = ["title"]
    exclude = ["slug", "created_at"]


class CategoryEntryAdmin(admin.ModelAdmin):
    list_display = ["category", "language_code","created_at"]
    list_filter = ["category"]
    exclude = ["created_at"]


class LinkInlineAdmin(admin.TabularInline):
    model = Link
    extra = 1


class CommonEntryAdmin(admin.ModelAdmin):
    list_display = ["title", "page", "language_code","created_at"]
    list_filter = ["page"]
    search_fields = ["title"]
    exclude = ["created_at"]
    inlines = [LinkInlineAdmin]


admin.site.register(NewsEntry, NewsEntryAdmin)
admin.site.register(CategoryEntry, CategoryEntryAdmin)
admin.site.register(CommonEntry, CommonEntryAdmin)
