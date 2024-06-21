from django.contrib import admin

from apps.names.models import Name


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ("name", "meaning", "origin")
    search_fields = ("name", "meaning")
