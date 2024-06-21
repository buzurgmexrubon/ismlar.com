from django.urls import path

from apps.names.views import names_list

app_name = "names"

urlpatterns = [
    path("", names_list, name="names_list"),
]
