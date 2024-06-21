from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve


urlpatterns = [
    path("", include("apps.common.urls", namespace="common")),
    path("continents/", include("apps.continents.urls", namespace="continents")),
    path("origins/", include("apps.origins.urls", namespace="origins")),
    path("names/", include("apps.names.urls", namespace="names")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
