from django.contrib import admin

from apps.origins.models import Origin


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
