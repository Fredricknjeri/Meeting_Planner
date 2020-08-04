from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from meetings.models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    # to get a 404 page when an id that does not exist is entered

    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all()})



MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid(): #always use this to validated.. for securitu purposes
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

RoomForm = modelform_factory(Room, exclude=[])

def add_room(request):
    if request.method == "POST":
        room_form = RoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
            return redirect("rooms")
    else:
        room_form = RoomForm()
    return render(request, "meetings/add_room.html", {"room_form": room_form})

