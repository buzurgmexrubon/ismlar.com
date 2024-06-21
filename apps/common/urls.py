from django.urls import path

from apps.common.views import home

app_name = "common"

urlpatterns = [
    path("", home, name="home"),
]
