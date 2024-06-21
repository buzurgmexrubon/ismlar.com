from django.shortcuts import render


# Create your views here.
def names_list(request):
    return render(request, "names/name_list.html")
