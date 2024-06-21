from django.shortcuts import render


# Create your views here.
def origin_list(request):
    return render(request, "origins/origin_list.html")
