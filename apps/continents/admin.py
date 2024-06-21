from django.contrib import admin

from apps.continents.models import Continent


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
