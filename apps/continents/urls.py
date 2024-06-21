from django.urls import path

from apps.continents.views import continent_list

app_name = "continents"

urlpatterns = [
    path("", continent_list, name="continent_list"),
]
