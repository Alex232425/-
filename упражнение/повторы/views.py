from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Главная страница</h4>")


def about(request):
    return HttpResponse("<h4>О нашей компании!</h4>")



def location(request):
    return HttpResponse("<h4>Наш адрес и местонахождения:</h4>")

