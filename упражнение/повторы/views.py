from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "повторы/index.html")


def about(request):
    return render(request, "повторы/about.html")



def location(request):
    return HttpResponse("<h4>Наш адрес и местонахождения:</h4>")

