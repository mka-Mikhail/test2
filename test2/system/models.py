from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True, null=True)
    time_created = models.TimeField(auto_now_add=True, null=True)
    date_updated = models.DateField(auto_now_add=True, null=True)
    time_updated = models.TimeField(auto_now_add=True, null=True)
