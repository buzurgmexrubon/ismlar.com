from django.urls import path

from apps.origins.views import origin_list

app_name = "origins"

urlpatterns = [
    path("", origin_list, name="origin_list"),
]
