from django.shortcuts import render

from apps.names.models import Name
from apps.origins.models import Origin


def home_page(request):
    names = Name.objects.all()
    origins = Origin.objects.all()
    context = {
        "names": names,
        "origins": origins,
    }

    return render(request, "home.html", context)
