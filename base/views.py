from django.shortcuts import render


rooms = [
    {"id": 1, "name": "Lets learn Python"},
    {"id": 2, "name": "Lets learn Javascript"},
    {"id": 3, "name": "Lets learn Html"},
    {"id": 4, "name": "Lets learn Css"},
    {"id": 5, "name": "Lets learn Django"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/index.html", context)


def room(request, pk):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i
    context = {"room": room}
    return render(request, "base/room.html", context)
