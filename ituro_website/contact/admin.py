from django.contrib import admin
from contact.models import TeamMember, Team


class TeamMemberInlineAdmin(admin.TabularInline):
    model = TeamMember


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "language_code", "created_at"]
    list_filter = ["created_at",]
    search_fields = ["name",]
    exclude = ["created_at", ]
    inlines = [TeamMemberInlineAdmin]


admin.site.register(Team, TeamAdmin)
