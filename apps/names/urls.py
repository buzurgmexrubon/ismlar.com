from django.urls import path

from apps.names.views import (
    names_list,
    get_top100,
    get_search,
    get_origins,
    get_favorites,
    get_most_searched,
    get_suggest_name,
    get_gender,
    get_alphabetically,
    get_detail_name,
    get_collections,
    like_name,
)

app_name = "names"

urlpatterns = [
    path("", names_list, name="names_list"),
    path("like/<int:name_id>/", like_name, name="like_name"),
    path("name/<str:name>", get_detail_name, name="detail"),
    path("top100", get_top100, name="top100"),
    path("top100/<str:gender>", get_top100, name="top100"),
    path("search", get_search, name="search"),
    path("origins", get_origins, name="origins"),
    path("origins/<str:origin_name>", get_origins, name="origin_by_name"),
    path("collections", get_collections, name="collections"),
    path("favorites", get_favorites, name="favorites"),
    path("most_searched", get_most_searched, name="most_searched"),
    path("suggest_name", get_suggest_name, name="suggest_name"),
    path("suggest_name/<str:suggested_name>", get_suggest_name, name="suggest_name"),
    path("<str:gender>", get_gender, name="gender"),
    path("<str:gender>/<str:letter>", get_alphabetically, name="alphabetically"),
]
