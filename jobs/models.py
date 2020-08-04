from django.db import models

class Job (models.Model):
    jobTitle = models.CharField(max_length=500)
    jobPosition = models.CharField(max_length=200)
    experience = models.IntegerField()
