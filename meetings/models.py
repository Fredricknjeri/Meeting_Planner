from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=200)
    floorNo = models.IntegerField(default=1)
    roomNo = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} on {self.floorNo}st Floor"



class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"