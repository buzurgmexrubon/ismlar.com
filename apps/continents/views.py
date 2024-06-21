from django.shortcuts import render


# Create your views here.
def continent_list(request):
    return render(request, "continents/continent_list.html")
