from django.shortcuts import render
from .models import Room
from .forms import RoomForm

rooms = [
    {"id": 1, "name": "Lets learn Python"},
    {"id": 2, "name": "Lets learn Javascript"},
    {"id": 3, "name": "Lets learn Html"},
    {"id": 4, "name": "Lets learn Css"},
    {"id": 5, "name": "Lets learn Django"},
]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/index.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()
    context = {"form": form}
    return render(request, "base/room_form.html", context)
