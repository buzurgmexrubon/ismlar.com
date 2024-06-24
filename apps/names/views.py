from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from apps.names.models import Name, Like
from apps.origins.models import Origin


@login_required
def like_name(request, name_id):
    name = get_object_or_404(Name, pk=name_id)
    user = request.user  # Get the currently logged-in user

    # Check if user has already liked the name
    like = Like.objects.filter(user=user, name=name).first()

    if like:
        like.delete()
        liked = False  # Set liked flag for response
    else:
        Like.objects.create(user=user, name=name)
        liked = True  # Set liked flag for response

    like_count = name.like_set.count()  # Get total likes for the name

    # Return JSON response with like status and like count
    return JsonResponse({"liked": liked, "like_count": like_count})


# Create your views here.
def names_list(request):
    context = {}
    return render(request, "names/name_list.html", context)


def get_detail_name(request, name):
    context = {
        "name": name,
        "user": request.user,
    }
    return render(request, "names/detail.html", context)


def get_top100(request, gender=None):
    if gender:
        context = {
            "gender": gender,
        }
    else:
        context = {}
    return render(request, "names/top100.html", context)


def get_search(request):
    context = {}
    return render(request, "names/search.html", context)


def get_origins(request, origin_name=None):
    if origin_name is None:
        origins = Origin.objects.all()
        names = Name.objects.filter(origin__name=origin_name)
        origin_names_count = len(names)
    else:
        origins = Origin.objects.filter(name=origin_name)
        names = []
        origin_names_count = len(names)
    context = {
        "names": names,
        "origins": origins,
        "origin_name": origin_name,
        "origin_names_count": origin_names_count,
    }
    return render(request, "names/origins.html", context)


def get_collections(request):
    context = {}
    return render(request, "names/collections.html", context)


def get_origins_by_name(request, origin):
    context = {
        "origin": origin,
    }
    return render(request, "names/origins.html", context)


def get_favorites(request):
    context = {}
    return render(request, "names/favorites.html", context)


def get_most_searched(request):
    context = {}
    return render(request, "names/most_searched.html", context)


def get_suggest_name(request, suggested_name):
    names = Name.objects.filter(name__name=suggested_name)
    context = {
        "names": names,
        "suggested_name": suggested_name,
    }
    return render(request, "names/suggest_name.html", context)


def get_gender(request, gender):
    names = Name.objects.filter(gender=gender)
    origins = Origin.objects.all()
    context = {
        "names": names,
        "gender": gender,
        "origins": origins,
    }
    return render(request, "names/gender.html", context)


def get_alphabetically(request, gender, letter):
    context = {
        "gender": gender,
        "letter": letter,
    }
    return render(request, "names/alphabetically.html", context)
