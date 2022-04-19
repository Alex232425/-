from django.shortcuts import render



def index(request):
    return render(request, "повторы/index.html")


def about(request):
    return render(request, "повторы/about.html")



def location(request):
    return render(request, "повторы/location.html")

