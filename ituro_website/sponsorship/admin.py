from django.contrib import admin
from sponsorship.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ["name", "sponsor_type", "language_code", "created_at"]
    list_filter = ["sponsor_type"]
    search_fields = ["name"]
    exclude = ["created_at"]


admin.site.register(Sponsor, SponsorAdmin)
