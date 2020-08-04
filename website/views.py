from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})
def home(request):
    return HttpResponse("This is your Homepage")

def date(request):

    return HttpResponse('This page was served at:' + str(datetime.now()))

def about(request):
    return HttpResponse('My name is Fredrick Njeri,\n email: fredricknjeri64@gmail.com \n phone: 0711625220')