from django.shortcuts import render


def home(request):
    return HttpResponse("Home page")


def room(request):
    return HttpResponse("Room")
